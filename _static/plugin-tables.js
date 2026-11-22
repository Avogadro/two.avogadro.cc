// Fills the tables on docs/plugins/available.html from live JSON.
// Plugin metadata is third-party: build DOM with textContent only.
const PLUGINS_URL = "https://avogadro.cc/plugins2.json";
const STATS_URL = "https://plugins.avogadro.cc/stats?days=30";
const ERROR_LINK = "https://github.com/Avogadro/plugins";
// Nearly every user installs these, so they would always top the list
const NOT_RANKED = new Set(["generators"]);

// PEP 503 normalization, minus the "avogadro-" prefix (matches the generator)
function statsKey(name) {
  const key = String(name).toLowerCase().replace(/[-_.]+/g, "-");
  return key.startsWith("avogadro-") ? key.slice("avogadro-".length) : key;
}

// Same prefixes, longest first, as PackageModel::displayName() in avogadrolibs
const AVO_PREFIXES = ["avogadro-", "avogadro_", "avogadro", "avo-", "avo_", "avo"];

// Drop the redundant "avogadro-" / "avo_" etc. prefix, as the GUI does
function displayName(name) {
  const text = String(name);
  const lower = text.toLowerCase();
  const prefix = AVO_PREFIXES.find((p) => lower.startsWith(p));
  const stripped = prefix ? text.slice(prefix.length) : text;
  return stripped || text;
}

function parseDate(plugin) {
  const t = Date.parse(plugin["date-added"]);
  return Number.isNaN(t) ? null : t;
}

function newest(plugins, count = 10) {
  return plugins
    .map((p) => ({ plugin: p, time: parseDate(p) }))
    .filter((e) => e.time !== null)
    .sort((a, b) => b.time - a.time || a.plugin.name.localeCompare(b.plugin.name))
    .slice(0, count);
}

function popular(plugins, stats, count = 10) {
  return plugins
    .filter((p) => stats[statsKey(p.name)] && !NOT_RANKED.has(statsKey(p.name)))
    .map((p) => ({ plugin: p, recent: stats[statsKey(p.name)].recent || 0 }))
    .sort((a, b) => b.recent - a.recent || a.plugin.name.localeCompare(b.plugin.name))
    .slice(0, count);
}

function safeUrl(value) {
  try {
    const url = new URL(value);
    return url.protocol === "https:" ? url.href : null;
  } catch (e) {
    return null;
  }
}

function cell(row, content) {
  const td = row.insertCell();
  if (content instanceof Node) td.appendChild(content);
  else td.textContent = content;
  return td;
}

function nameNode(plugin) {
  const href = safeUrl((plugin.git || {}).repo) || safeUrl(plugin["readme-url"]);
  const label = displayName(plugin.name);
  if (!href) return document.createTextNode(label);
  const a = document.createElement("a");
  a.href = href;
  a.className = "reference external";
  a.textContent = label;
  return a;
}

function showMessage(id, text, withLink) {
  const table = document.getElementById(id);
  const msg = document.getElementById(id + "-status");
  table.hidden = true;
  msg.hidden = false;
  msg.textContent = text;
  if (withLink) {
    const a = document.createElement("a");
    a.href = ERROR_LINK;
    a.textContent = "Avogadro plugins on GitHub";
    msg.append(" See ", a, ".");
  }
}

function fill(id, rows) {
  const table = document.getElementById(id);
  const body = table.tBodies[0];
  body.replaceChildren();
  for (const cells of rows) {
    const row = body.insertRow();
    for (const c of cells) cell(row, c);
  }
  document.getElementById(id + "-status").hidden = true;
  table.hidden = false;
}

async function getJson(url) {
  const response = await fetch(url, { cache: "no-cache" });
  if (!response.ok) throw new Error(url + ": " + response.status);
  return response.json();
}

async function init() {
  if (!document.getElementById("plugins-newest")) return;
  // Hidden in the markup so that "Loading…" never shows without JavaScript
  for (const id of ["plugins-newest", "plugins-popular"]) {
    const status = document.getElementById(id + "-status");
    if (status) status.hidden = false;
  }
  const pluginsPromise = getJson(PLUGINS_URL);
  const statsPromise = getJson(STATS_URL);

  pluginsPromise.then((plugins) => {
    const rows = newest(plugins).map((e) => [
      nameNode(e.plugin),
      e.plugin.description || "",
      new Date(e.time).toISOString().slice(0, 10),
    ]);
    if (rows.length) fill("plugins-newest", rows);
    else showMessage("plugins-newest", "Dates added are not available yet.", false);
  }).catch(() => showMessage("plugins-newest", "Could not load plugin data.", true));

  Promise.all([pluginsPromise, statsPromise]).then(([plugins, stats]) => {
    const rows = popular(plugins, stats.plugins || {}).map((e, i) => [
      String(i + 1),
      nameNode(e.plugin),
      e.plugin.description || "",
      String(e.recent),
    ]);
    fill("plugins-popular", rows);
  }).catch(() => showMessage("plugins-popular", "Could not load plugin data.", true));
}

if (typeof document !== "undefined") init();
if (typeof module !== "undefined") module.exports = { statsKey, displayName, newest, popular, safeUrl };

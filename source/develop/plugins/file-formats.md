(develop-plugins-file-formats)=

# File format plugins

A file format plugin is declared with a `[[tool.avogadro.file-formats]]`
entry in the plugin's `pyproject.toml` (or `avogadro.toml`).

```toml
[[tool.avogadro.file-formats]]
identifier = "cp2k"
format-name = "CP2K"
file-extensions = ["out", "log", "cp2k"]
description = "Read CP2K main output files"
support.read = true
support.write = false
output-format = "cjson"
input-mode = "file"
bond = true
patterns = ["CP2K| version string"]
```

| Key                | Type              | Meaning |
| ---                | ---               | --- |
| `identifier`       | string            | Unique identifier for the format (required) |
| `format-name`      | string            | User-friendly name (required) |
| `description`      | string            | Description and help text for users |
| `file-extensions`  | array of strings  | Extensions the format reads and/or writes |
| `mime-types`       | array of strings  | MIME types for the format |
| `support.read`, `support.write` | boolean | Which operations the plugin implements |
| `output-format`    | string            | Format the plugin produces when reading (e.g. `"cjson"`) |
| `input-format`     | string            | Format the plugin receives when writing |
| `input-mode`, `output-mode` | string   | `"string"` (default) or `"file"` |
| `bond`             | boolean           | Ask Avogadro to perceive bonds after reading |
| `patterns`         | array of strings, or a string | Text that identifies the format by content (see below) |

## Identifying a format by content: `patterns`

Programs such as Gaussian, ORCA, CP2K or Psi4 all write their output to
generic files like `output.out` or `job.log`, so the file extension alone
cannot say which reader to use. Avogadro's generic output reader looks inside
the file instead. A plugin can take part by listing `patterns`:

- Each pattern is a **literal substring**, not a regular expression. Matching
  is case-sensitive and is done one line at a time.
- A file matches the plugin if **any one** pattern occurs in **any one** line.
- `patterns` may be an array of strings, or a single string (treated as a list
  of one). Empty or whitespace-only entries are ignored.
- Choose text the program always prints near the top of its output, such as a
  version banner, and that other programs are unlikely to print.

Patterns are only consulted for the generic output extensions handled by
Avogadro's generic output reader: `out`, `output` and `log`. They do not
change how other extensions are routed, and a plugin should still list the
extensions it supports in `file-extensions`.

The file is scanned from the top, line by line. Avogadro's built-in readers
(NWChem, GAMESS-US, Molden, ORCA and xtb) are checked first on each line, then
the plugins' patterns. The earliest matching line in the file wins; if several
plugins match the same line, the one registered first is used. If no pattern
matches, Avogadro falls back to the cclib plugin and then Open Babel, as
before.

Older versions of Avogadro ignore the `patterns` key, so it is safe to include
it in a plugin that must also work with them.

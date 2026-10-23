# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import date
import requests

# -- Project information -----------------------------------------------------

project = 'Avogadro'
author = 'The OpenChemistry / Avogadro Teams'
# The latest version from the GitHub API
try:
    response = requests.get("https://api.github.com/repos/openchemistry/avogadrolibs/releases/latest")
    release = response.json()['tag_name']
except requests.exceptions.ConnectionError:
    release = "2.1.0"
version = release

year = date.today().year
copyright = f'©{year} {author}'



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinxext.rediraffe',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'breathe',
    'myst_parser',
    'sphinxcontrib.mermaid',
]

# Only load pydata_sphinx_theme as an extension for HTML builds;
# its translator crashes the LaTeX builder.
import sys
if not any(b in sys.argv for b in ('latex', 'latexpdf', 'qthelp')):
    extensions.append('pydata_sphinx_theme')

# True when building the PDF (LaTeX) output
is_latex_build = any(b in sys.argv for b in ('latex', 'latexpdf'))
if is_latex_build:
    # Convert the SVG images (tool icons, etc.) to vector PDF with rsvg-convert
    extensions.append('sphinxcontrib.rsvgconverter')

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# set up redirects
rediraffe_branch = 'main'
rediraffe_redirects = "redirects.txt"

# sphinx-design's fontawesome (v4) conflicts with Sphinx's fontawesome5 in LaTeX.
# Disable it here; Sphinx handles admonition icons via fontawesome5 on its own.
sd_fontawesome_latex = False

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = 'docs'    # one file
language = "en"             # default language

myst_substitutions = {
  "release": release,
  "macurl": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-{version}-Darwin.dmg",
  "macarmurl": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-{version}-Darwin-arm64.dmg",
  "winurl": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-{version}-win64.exe",
  "appurl": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-x86_64.AppImage",
  "sourceurl": f"https://github.com/OpenChemistry/avogadrolibs/archive/refs/tags/{version}.zip",
}

myst_url_schemes = {
    "http": None,
    "https": None,
    "release": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-{version}-" + "{{file}}",
    "release-no-version": f"https://github.com/OpenChemistry/avogadrolibs/releases/download/{version}/Avogadro2-" + "{{file}}",
    "source": f"https://github.com/OpenChemistry/avogadrolibs/archive/refs/tags/{version}" + "{{file}}",
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

if is_latex_build:
    # The API reference pages (generated from the doxygen XML by breathe) are
    # HTML-only; they are hundreds of pages and need the doxygen XML to build.
    exclude_patterns.append('develop/class/*')

# Add Open Babel and maybe RDKit too?
#intersphinx_mapping = {
#    'python' : ('https://docs.python.org/3/', None),
#    'numpy'  : ('https://numpy.org/doc/stable/', None)
#}

# -- Options for Breathe --------

breathe_projects = { 'AvogadroLibs': '../../build/avogadrolibs/docs/xml' }
breathe_default_project = 'AvogadroLibs'
breathe_default_members = ('members', 'undoc-members', 'protected-members')

# -- Options for LaTeX / PDF output ------------------------------------------
# The PDF is built with LuaLaTeX (Unicode engine), which needs:
#   * TeX Live packages: fontspec, luaotfload, lm, fontawesome5, mhchem,
#     newunicodechar (see .github/workflows/build-pdf.yml for the full list)
#   * Noto fonts (Debian/Ubuntu: fonts-noto-core, fonts-noto-cjk) for
#     sub/superscripts, math symbols, Tamil, Arabic and CJK, which Latin
#     Modern lacks

latex_engine = 'lualatex'

latex_documents = [
    ('latex-index', 'Avogadro.tex', 'Avogadro Documentation',
     'The OpenChemistry / Avogadro Teams', 'manual'),
]

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    # Latin Modern for text. Characters it lacks (arrows, math symbols,
    # Tamil, Arabic, ...) fall back, glyph by glyph, to the Noto fonts.
    'fontpkg': r"""
\usepackage{fontspec}
\directlua{
  luaotfload.add_fallback("avofallback", {
    "Noto Sans:mode=harf;",
    "Noto Sans Math:mode=harf;",
    "Noto Sans Symbols:mode=harf;",
    "Noto Sans Symbols 2:mode=harf;",
    "Noto Sans Tamil:mode=harf;script=taml;",
    "Noto Naskh Arabic:mode=harf;script=arab;",
    "Noto Sans CJK SC:mode=harf;",
  })
}
\setmainfont{Latin Modern Roman}[RawFeature={fallback=avofallback}]
\setsansfont{Latin Modern Sans}[RawFeature={fallback=avofallback}]
\setmonofont{Latin Modern Mono}[RawFeature={fallback=avofallback}]
""",
    'preamble': r"""
% Scale all images to 50% of their default size
\let\origsphinxincludegraphics\sphinxincludegraphics
\renewcommand{\sphinxincludegraphics}[2][]{%
  \origsphinxincludegraphics[scale=0.5,#1]{#2}%
}

% Chemical formulas: \ce{...} (rendered by MathJax in HTML)
\usepackage[version=4]{mhchem}

% Emoji used in the text: map them to FontAwesome icons rather than
% requiring a colour emoji font
\usepackage{fontawesome5}
\usepackage{newunicodechar}
\newunicodechar{📄}{\faFile}
\newunicodechar{⚡}{\faBolt}
\newunicodechar{⚛}{\faAtom}
\newunicodechar{🔒}{\faLock}
\newunicodechar{☰}{\faBars}
\newunicodechar{➕}{\faPlus}
\newunicodechar{✅}{\faCheck}
\newunicodechar{📁}{\faFolder}
\newunicodechar{🛑}{\faStopCircle}
\newunicodechar{❗}{\faExclamation}
""",
    # Avoid blank pages between chapters
    'extraclassoptions': 'openany,oneside',
    'tocdepth': 2,
    # sphinx-design's FontAwesome v4 conflicts with Sphinx's fontawesome5
    'sphinxsetup': 'iconpackage=fontawesome5',
}

# Sphinx's default 'colorrows' table style (zebra stripes) overrides colortbl's
# \CT@everycr; with array >= 2026/02/24 (TeX Live 2026) colortbl no longer
# keeps that token list separate from \everycr, so Sphinx's hack recurses
# forever ("TeX capacity exceeded, input stack size") at the first table.
latex_table_style = ['booktabs']

latex_logo = '_static/avogadro2.png'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False

html_baseurl = 'https://avogadro.cc'

html_theme_options = {
    'external_links': [
        {'name': 'Discuss', 'url': 'https://discuss.avogadro.cc'}
    ],
    'footer_start': ['copyright', 'contribute', 'sphinx-version' ],
    'github_url': 'https://github.com/openchemistry/avogadrolibs',
    'use_edit_page_button': True,
    'show_toc_level': 2,
    'announcement': "Please see the results of our <a href='https://discuss.avogadro.cc/t/avogadro-2026-survey-results/7502'>anonymous community survey</a> - more feedback welcome!",
    "header_links_before_dropdown": 6,
    'collapse_navigation': True,
    "logo": {
        "alt_text": "Avogadro Documentation- Home",
        "image_light": "_static/avogadro2.png",
        "image_dark": "_static/avogadro2-dark.png",
    },
    "icon_links": [
        {
            "name": "Bluesky",
            "url": "https://bsky.app/profile/avogadro.cc",
            "icon": "fa-brands fa-bluesky",
        },
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@avogadrochem",
            "icon": "fa-brands fa-mastodon",
        },
    ],
}

html_context = {
    # 'github_url': 'https://github.com', # or your GitHub Enterprise interprise
    'github_user': 'avogadro',
    'github_repo': 'two.avogadro.cc',
    'github_version': 'main',
    'doc_path': 'source/',
}

html_sidebars = {
    # omit the sidebar on the mainpage
  #'index': []
}

html_logo = '_static/avogadro2.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_css_files = [
    'custom.css',
    'mermaid-theme.css',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- PDF section hierarchy ---------------------------------------------------
# The index pages of the four top-level parts (docs, develop, contrib, teach)
# end with a hidden toctree, after some "##" headings. docutils places that
# toctree inside the last open section, so in LaTeX every child document would
# be nested under whatever heading happens to come last. For the PDF only,
# flatten the subsections of such a page into unnumbered headings (rubrics) so
# the toctree is a direct child of the page's top-level section and the child
# documents become proper sections of the chapter. HTML is not affected.

def _flatten_section(section):
    """Return the section's title as a rubric, then its body, recursively."""
    from docutils import nodes

    rubric = nodes.rubric(rawsource=section.rawsource)
    rubric.extend(section[0].children)
    # keep the ids/names, so labels and heading anchors still resolve
    for key in ('ids', 'names', 'dupnames', 'classes'):
        rubric[key] = list(section.get(key, []))
    flat = [rubric]
    if rubric['ids']:
        # the LaTeX writer emits no \label for a rubric, so add a target for
        # the same ids in front of it, to keep {ref} links into it working
        flat.insert(0, nodes.target('', '', ids=list(rubric['ids'])))
    for child in section.children[1:]:
        if isinstance(child, nodes.section):
            flat.extend(_flatten_section(child))
        else:
            flat.append(child)
    return flat


def _flatten_nested_toctree_sections(app, doctree):
    """doctree-read handler: lift toctrees out of subsections (LaTeX only)."""
    from docutils import nodes
    from sphinx import addnodes

    if app.builder.format != 'latex':
        return
    top = next((n for n in doctree.children if isinstance(n, nodes.section)),
               None)
    if top is None:
        return
    # only documents with a toctree nested below the top-level section, and
    # with child documents to put in its place (not just "self" or URLs)
    docname = app.env.docname
    if not any(next((a for a in _ancestors(t)
                     if isinstance(a, nodes.section)), None) is not top
               and any(ref in app.env.found_docs and ref != docname
                       for _, ref in t['entries'])
               for t in doctree.findall(addnodes.toctree)):
        return

    children = []
    for child in top.children:
        if isinstance(child, nodes.section):
            children.extend(_flatten_section(child))
        else:
            children.append(child)
    top.children = []
    top.extend(children)
    # point the document's id lookup at the new rubric nodes
    for rubric in top.findall(nodes.rubric):
        for id_ in rubric['ids']:
            doctree.ids[id_] = rubric


def _ancestors(node):
    node = node.parent
    while node is not None:
        yield node
        node = node.parent


def setup(app):
    # run before the toc/domain collectors so they see the flattened tree
    app.connect('doctree-read', _flatten_nested_toctree_sections, priority=1)

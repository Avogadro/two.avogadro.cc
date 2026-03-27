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
    release = "1.103.0"
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

# FontAwesome icons in LaTeX / PDF output (overridden below for minimal TeX installs)
sd_fontawesome_latex = True

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

latex_documents = [
    ('latex-index', 'Avogadro.tex', 'Avogadro Documentation',
     'The OpenChemistry / Avogadro Teams', 'manual'),
]

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': r'''
% Scale all images to 50% of their default size
\let\origsphinxincludegraphics\sphinxincludegraphics
\renewcommand{\sphinxincludegraphics}[2][]{%
  \origsphinxincludegraphics[scale=0.5,#1]{#2}%
}
''',
    # Avoid blank pages between chapters
    'extraclassoptions': 'openany,oneside',
    'tocdepth': 2,
}

# FontAwesome / font availability depends on the TeX installation.
# CI has full texlive (fontawesome5); local basic installs may not.
import subprocess
def _has_tex_package(name):
    """Check if a TeX package (.sty) is available."""
    try:
        result = subprocess.run(
            ['kpsewhich', f'{name}.sty'],
            capture_output=True, timeout=5)
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

if _has_tex_package('fontawesome5'):
    # Full TeX install — explicitly use fontawesome5 to avoid conflicts
    latex_elements['sphinxsetup'] = 'iconpackage=fontawesome5'
elif not _has_tex_package('fontawesome'):
    # Minimal TeX install — disable icon fonts and use OT1/Computer Modern
    latex_elements['fontenc'] = r'\usepackage[OT1]{fontenc}'
    latex_elements['fontpkg'] = ''
    latex_elements['sphinxsetup'] = 'iconpackage=none'
    sd_fontawesome_latex = False

latex_logo = '_static/avogadro2.png'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False

html_baseurl = 'https://two.avogadro.cc'

html_theme_options = {
    'external_links': [
        {'name': 'Discuss', 'url': 'https://discuss.avogadro.cc'}
    ],
    'footer_start': ['copyright', 'contribute', 'sphinx-version' ],
    'github_url': 'https://github.com/openchemistry/avogadrolibs',
    'use_edit_page_button': True,
    'show_toc_level': 2,
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

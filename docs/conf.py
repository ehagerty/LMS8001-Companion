# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import sphinx_rtd_theme
import requests
import warnings
from pathlib import Path
from urllib.parse import urljoin

# -- Path setup --------------------------------------------------------------
# Put config directory first on sys.path so imports from this work

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# -- MyriadRF configuration --------------------------------------------------

# Path to remote assets
asset_base = 'https://assets.myriadrf.net/sphinx/'

# Import the project config from project.py
import project as project_cfg

# Assign project config variables to local names
project = project_cfg.project 
copyright = project_cfg.copyright
author  = project_cfg.author
release = project_cfg.release

# Set the CSS to use
if not project_cfg.archived:
    html_css_files = [urljoin(asset_base, 'mr-custom.css')]
else:
    html_css_files = [urljoin(asset_base, 'mr-archived.css')]

# Retrieve remote asset
def _fetch_remote(path, base=asset_base, timeout=10, default=""):
    url = urljoin(base, path)
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as exc:
        warnings.warn(f"Failed to fetch {url}: {exc}")
        return default
    
# Read local asset 
def _read_local(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except Exception:
        return ""

# Get remote custom footer and navbar and
# global substitutions and external links
extrabody_content = _fetch_remote('mr-navbar.html')
extrafooter_content = _fetch_remote('mr-footer.html')
global_subs = _fetch_remote('substitutions.conf')
global_extlinks = _fetch_remote('extlinks.conf')

# Get local substitutions and external links
local_subs = _read_local(HERE / 'substitutions.conf')
local_extlinks = _read_local(HERE / 'extlinks.conf')

# HTML customisation 
html_context = {
    'extrabody': extrabody_content,
    'extrafooter': extrafooter_content,
    'display_github': True,
    'github_user': 'myriadrf',
    'github_repo': project_cfg.github_repo,
    'github_version': project_cfg.github_repo_path,
    'archived': project_cfg.archived
}

# Merge remote + local RST epilog content
parts = []

if global_subs:
    parts.append(global_subs.rstrip() + "\n")
if local_subs:
    parts.append(local_subs.rstrip() + "\n")
if global_extlinks:
    parts.append(global_extlinks.rstrip() + "\n")
if local_extlinks:
    parts.append(local_extlinks.rstrip() + "\n")

if parts:
    rst_epilog = "\n".join(parts)
else:
    # Fallback: if nothing was found/read, keep original include-style epilog 
    # so that Sphinx can try to include files by path.
    rst_epilog = """
.. include:: /substitutions.conf
.. include:: /extlinks.conf
"""

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx-mathjax-offline',
    'sphinx_code_tabs',
    'sphinx_rtd_theme',
    'notfound.extension'
]

# Allow same section headings and thus labels to be used across documents.
autosectionlabel_prefix_document = True

# Paths that contain templates
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'logo_only': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 5
}

html_show_sphinx = False

# HTML last updated formatting
html_last_updated_fmt = '%b %d, %Y'

root_doc = 'index'


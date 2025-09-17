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

import sphinx_rtd_theme
import requests

# -- Get MyriadRF customisation assets -----------------------------------------

def fetch_remote_content(url):
    try:
        response = requests.get(url, verify=True)  # Using proper SSL verification
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

extrabody_content = fetch_remote_content('https://myriad-rtd-assets.netlify.app/navbar.html')
extrafooter_content = fetch_remote_content('https://myriad-rtd-assets.netlify.app/footer.html')

# -- Project configuration -----------------------------------------------------

# Basic configuration. Release should be updated for each release!

project = 'LMS8001 Companion'
copyright = '2025 Lime Microsystems'
author = 'Lime Microsystems'
release = '3v2'

# github_repo and github_version are used for the "Edit on GitHub" links.
# github_version should be set to the branch + path to the docs directory.
# The other variables should not be changed!

html_context = {
    'extrabody': extrabody_content,
    'extrafooter': extrafooter_content,
    'display_github': True,
    'github_user': 'myriadrf',
    'github_repo': 'LMS8001-Companion',
    'github_version': 'master/docs/'
}

highlight_language = 'console'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx-mathjax-offline',
    'sphinx_code_tabs',
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store']

# html_static_path = ['_static']

html_css_files = ['https://myriad-rtd-assets.netlify.app/mr-custom.css']

html_last_updated_fmt = '%b %d, %Y'

# Include external links and substitutions, such as for Unicode characters.
rst_epilog = """
.. include:: /substitutions.conf
.. include:: /extlinks.conf
"""

# Allow same section headings and thus labels to be used across documents.
autosectionlabel_prefix_document = True

# Generate SVG format images from LaTeX math embedded in RST documents.
#imgmath_image_format = 'svg'

# Default size of 12pt for equations is a bit small.
#imgmath_font_size = 16

#mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'logo_only': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 5
}

html_show_sphinx = False

root_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

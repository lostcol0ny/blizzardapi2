import sys
import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'blizzardapi2'
copyright = '2024, lostcol0ny'
author = 'lostcol0ny'
release = '0.1.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('.'))

templates_path = ['_templates']
exclude_patterns = [
    'sphinx.ext.autodoc',
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

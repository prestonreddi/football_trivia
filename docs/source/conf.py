import os
import sys
import django
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'football_trivia'
copyright = '2025, Preston'
author = 'Preston'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

# Absolute path to the root folder (which is named football_trivia)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Absolute path to your Django project folder (also football_trivia inside root)
project_folder = os.path.join(project_root, 'football_trivia')

# Add both to sys.path so Python can find your project and settings
sys.path.insert(0, project_root)
sys.path.insert(0, project_folder)

# Set environment variable to tell Django where settings are
os.environ['DJANGO_SETTINGS_MODULE'] = 'football_trivia.settings'

# Setup Django
django.setup()

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import importlib.metadata
import os
import sys
import tomllib

sys.path.insert(0, os.path.abspath("../package"))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

_DISTRIBUTION_METADATA = importlib.metadata.metadata("package")

author = _DISTRIBUTION_METADATA["Author"]
project = _DISTRIBUTION_METADATA["Name"]
version = _DISTRIBUTION_METADATA["Version"]
copyright = f"2023, {author}"
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
    "sphinx_substitution_extensions",
]
add_module_names = False
html_show_sourcelink = False
templates_path = ["_templates"]


# napoleon settings
napoleon_google_docstring = False
napoleon_include_private_with_doc = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    "DataFrame": "pandas.DataFrame",
    "Series": "pandas.Series",
    "Iterable": "typing.Iterable",
}
# autodoc settings
autoclass_content = "both"
autodoc_typehints_format = "short"
autodoc_inherit_docstrings = True
# autosummary settings
autosummary_generate = True
# sphinx_autodoc_typehints settings
set_type_checking_flag = True
# intersphinx settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

with open("../pyproject.toml", "rb") as f:
    file = tomllib.load(f)
min_python_version = file["tool"]["poetry"]["dependencies"]["python"].replace("^", "")
rst_prolog = f"""
.. |release| replace:: {version}
.. |min_python_version| replace:: {min_python_version}
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinxawesome_theme"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 3,
    "style_external_links": False,
}
html_show_sphinx = False
html_show_copyright = False
html_logo = "_static/python.svg"
html_static_path = ["_static"]

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FlyingFish'
copyright = 'v0.1'
author = 'yu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_markdown_tables',
    'sphinx.ext.githubpages',
    'sphinx_copybutton',
    'sphinx.ext.mathjax',
    'myst_parser'
]

myst_enable_extensions = [
    "amsmath",
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
    "tasklist"
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

pygments_style = 'sphinx'

latex_engine = "xelatex"
latex_use_xindy = False
latex_elements = {
    "preamble": "\\usepackage[UTF8]{ctex}\n",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme = 'alabaster'
html_static_path = ['_static']

html_logo = '_static/yu.png'
html_favicon = '_static/yu.png'

html_theme_options = {
#   "show_nav_level": 4,
    #"footer_start": ["author"],
    #"footer_center":[],
    #"footer_end":["author"],
}
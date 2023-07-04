#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ctapipe documentation build configuration file, created by
# sphinx-quickstart on Fri Jan  6 10:22:58 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------
import datetime
import os

# Get configuration information from setup.cfg
from configparser import ConfigParser

import pydata_sphinx_theme
import ctapipe

setup_cfg = ConfigParser()
setup_cfg.read([os.path.join(os.path.dirname(__file__), "..", "setup.cfg")])
setup_metadata = dict(setup_cfg.items("metadata"))
setup_options = dict(setup_cfg.items("options"))


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "nbsphinx",
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",
    "sphinx_design",
    "IPython.sphinxext.ipython_console_highlighting",
]


numpydoc_show_class_members = False
# numpydoc_class_members_toctree = False
nbsphinx_timeout = 200  # allow max 2 minutes to build each notebook


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


def setup(app):
    # fix trait aliases generating doc warnings
    from ctapipe.core import traits

    app.add_css_file("_static/ctapipe.css")

    aliases = [
        "flag",
        "observe",
        "Bool",
        "CRegExp",
        "CaselessStrEnum",
        "Dict",
        "Enum",
        "Float",
        "Int",
        "CInt",
        "Integer",
        "List",
        "Long",
        "Set",
        "TraitError",
        "Tuple",
        "Unicode",
        "UseEnum",
    ]
    for alias in aliases:
        getattr(traits, alias).__name__ = alias
        getattr(traits, alias).__module__ = "ctapipe.core.traits"


# These links are ignored in the checks, necessary due to broken intersphinx for
# these
nitpick_ignore = [
    ("py:class", "traitlets.config.configurable.Configurable"),
    ("py:class", "traitlets.traitlets.HasTraits"),
    ("py:class", "traitlets.traitlets.HasDescriptors"),
    ("py:class", "traitlets.traitlets.TraitType"),
    ("py:class", "traitlets.traitlets.BaseDescriptor"),
    ("py:class", "traitlets.traitlets.List"),
    ("py:class", "traitlets.traitlets.Container"),
    ("py:class", "traitlets.traitlets.Instance"),
    ("py:class", "traitlets.traitlets.ClassBasedTraitType"),
    ("py:class", "traitlets.traitlets.Int"),
    ("py:class", "traitlets.config.application.Application"),
    ("py:class", "traitlets.utils.sentinel.Sentinel"),
    ("py:class", "traitlets.traitlets.ObserveHandler"),
    ("py:obj", "traitlets.config.boolean_flag"),
    ("py:obj", "traitlets.TraitError"),
    ("py:obj", "-v"),  # fix for wrong syntax in a traitlets docstring
    ("py:meth", "MetaHasDescriptors.__init__"),
    ("py:meth", "HasTraits.__new__"),
    ("py:meth", "BaseDescriptor.instance_init"),
    ("py:obj", "cls"),
    ("py:obj", "name"),
    ("py:class", "astropy.coordinates.baseframe.BaseCoordinateFrame"),
    ("py:class", "astropy.table.table.Table"),
    ("py:class", "eventio.simtel.simtelfile.SimTelFile"),
    ("py:obj", "ctapipe.calib.CameraCalibrator"), # temporary fix to ignore warning
    ("py:obj", "ctapipe.calib.GainSelector"), # temporary fix to ignore warning
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# have all links automatically associated with the right domain.
default_role = "py:obj"

suppress_warnings = ["ref.citation"]  # ignore citation not referenced warnings

# General information about the project.

project = setup_metadata["name"]
author = setup_metadata["author"]
copyright = "{}.  Last updated {}".format(
    setup_metadata["author"], datetime.datetime.now().strftime("%d %b %Y %H:%M")
)
python_requires = setup_options["python_requires"]

# make some variables available to each page
rst_epilog = f"""
.. |python_requires| replace:: {python_requires}
"""

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

version = ctapipe.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "changes",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Version switcher -----------------------------------------------------

# Define the json_url for our version switcher.
json_url = "https://ctapipe.readthedocs.io/en/latest/_static/switcher.json"

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
if not version_match or version_match.isdigit():
    # For local development, infer the version to match from the package.
    release = ctapipe.__version__
    if "dev" in release or "rc" in release:
        version_match = "latest"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "_static/switcher.json"
    else:
        version_match = release


# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

html_theme = "pydata_sphinx_theme"
# html_theme_path = [pydata_sphinx_theme.__path__]


html_favicon = "_static/favicon.ico"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "logo": {
        "image_light": "ctapipe_logo.webp",
        "image_dark": "ctapipe_logo_dark.webp",
        "alt_text": "ctapipe",
    },
    "github_url": "https://github.com/cta-observatory/ctapipe",
    "header_links_before_dropdown": 6,
    "navbar_start": ["navbar-logo", "version-switcher"],
    "switcher": {
      "version_match": version_match,
      "json_url": json_url,
    },
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "CTA Observatory",
            "url": "https://www.cta-observatory.org/",
            "type": "url",
            "icon": "https://www.cta-observatory.org/wp-content/themes/ctao/favicon.ico"
        },
    ],
}

html_sidebars = {
    "**": ["sidebar-nav-bs.html", "sidebar-ethical-ads.html"],
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = ["_static"]
html_context = {
    "default_mode": "light",
    "github_user": "cta-observatory",
    "github_repo": "ctapipe",
    "github_version": "main",
    "doc_path": "docs",
}
html_css_files = ["ctapipe.css"]
html_file_suffix = ".html"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f"{project} v{release}"

# Output file base name for HTML help builder.
htmlhelp_basename = project + "doc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", project + ".tex", project + " Documentation", author, "manual")
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", project.lower(), project + " Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "ctapipe",
        "ctapipe Documentation",
        author,
        "ctapipe",
        "Experimental Data Analysis for the" "Cherenkov Telescope Array (CTA).",
        "Science",
    )
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "astropy": ("https://docs.astropy.org/en/latest/", None),
    "pytables": ("http://www.pytables.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "cython": ("https://docs.cython.org/en/latest/", None),
    "iminuit": ("https://iminuit.readthedocs.io/en/latest/", None),
    "traitlets": ("https://traitlets.readthedocs.io/en/stable/", None),
}

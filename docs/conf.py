"""
Configuration file for the Sphinx documentation builder.

# https://www.sphinx-doc.org/en/master/usage/configuration.html
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
"""

# import os
# import sys
# import django

# if os.getenv("READTHEDOCS", default=False) == "True":
#     sys.path.insert(0, os.path.abspath(".."))
#     os.environ["DJANGO_READ_DOT_ENV_FILE"] = "True"
#     os.environ["USE_DOCKER"] = "no"
# else:
#     sys.path.insert(0, os.path.abspath("/app"))
# os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
# os.environ["CELERY_BROKER_URL"] = os.getenv("REDIS_URL", "redis://redis:6379")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# django.setup()


# Project information

project = "Fandom Hub (API)"
copyright = "2024, Tyrone José"
author = "Tyrone José"

# General configs

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# Options for HTML output

html_theme = "alabaster"
html_static_path = ["_static"]

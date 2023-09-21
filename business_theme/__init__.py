"""Sphinx ReadTheDocs theme.
From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""
from os import path


__version__ = '0.1.0'
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('business_theme', path.abspath(path.dirname(__file__)))
    app.add_css_file('styles/main.css')

.. image:: https://raw.githubusercontent.com/Nekmo/sphinx-business-theme/master/logo.png
    :width: 100%

|


Sphinx Business Theme
#####################
Theme for Sphinx to create PDF files with a professional design. Use Weasyprint to generate the PDF file.
`Download example <https://github.com/Nekmo/sphinx-business-theme/releases/download/v0.0.0/Sphinx.Business.Theme.pdf>`_.

Installation
============
Install the latest version from the source code using::

   $ pip install -e git+git@https://github.com/Nekmo/sphinx-business-theme@master#egg=business_theme


Create documentation
====================
A `Cookicutter <https://github.com/cookiecutter/cookiecutter>`_ template is included to easily create new
documentation. Execute::

   $ create-docs

To generate a new PDF output::

   $ cd <documentation folder>
   $ make pdf



Demo project
============

You can play updating content inside `docs/demo` dir and making the pdf again as:

::

   cd docs/demo
   make pdf

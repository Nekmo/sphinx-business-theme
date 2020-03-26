.. image:: https://raw.githubusercontent.com/Nekmo/sphinx-business-theme/master/logo.png
    :width: 100%

|


Sphinx Business Theme
#####################
Theme for Sphinx to create PDF files with a professional design. Use Weasyprint to generate the PDF file.
`Download example <https://github.com/Nekmo/sphinx-business-theme/releases/download/v0.0.0/Sphinx.Business.Theme.pdf>`_.

Installation
============
Install the latest version from the source code using (you need previously `installed pip <https://pip.pypa
.io/en/stable/installing/>`_). Only `Python 3+ is supported <https://realpython.com/installing-python/>`_::

   pip3 install https://github.com/Nekmo/sphinx-business-theme/archive/master.tar.gz#egg=business_theme

Currently only tested on unix systems. The command must be executed in a terminal.

Create documentation
====================
A `Cookicutter <https://github.com/cookiecutter/cookiecutter>`_ template is included to easily create new
documentation. Execute in a terminal::

   $ create-docs

This command creates a new documentation directory. Go to the directory and run `make pdf` (only for unix) to create
a pdf::

   $ cd <documentation folder>
   $ make pdf

However, the pdf starts without content. Write your document by editing the files ``index.rst`` and ``readme.rst``.  The
syntax of the files is RestructuredText (rst). The syntax documentation is on the
`Sphinx website <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

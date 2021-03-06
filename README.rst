.. image:: https://raw.githubusercontent.com/Nekmo/sphinx-business-theme/master/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/travis/Nekmo/sphinx-business-theme.svg?style=flat-square&maxAge=2592000
  :target: https://travis-ci.org/Nekmo/sphinx-business-theme
  :alt: Latest Travis CI build status


Sphinx Business Theme
#####################
Theme for Sphinx to create PDF files with a professional design. This theme uses Weasyprint to generate the output to
PDF.
`A demo PDF is available <https://github.com/Nekmo/sphinx-business-theme/releases/latest/download/demo.pdf>`_.

Installation
============
Install the latest version from Pypi (you need previously `installed pip <https://pip.pypa
.io/en/stable/installing/>`_)::

    pip3 install -U sphinx-business-theme

You can also install the latest version from Github::

   pip3 install https://github.com/Nekmo/sphinx-business-theme/releases/latest/download/business_theme-0.1.0.tar.gz#egg=business_theme

Only `Python 3+ is supported <https://realpython.com/installing-python/>`_ Currently only tested on unix systems. The
command must be executed in a terminal. More info in the web documentation (or in the `pdf documentation
<https://github.com/Nekmo/sphinx-business-theme/releases/latest/download/docs.pdf>`_).


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

Read the docs on the web (or in `pdf <https://github.com/Nekmo/sphinx-business-theme/releases/latest/
download/docs.pdf>`_).

Demo project
============

You can play updating content inside `demo/` dir and making the pdf again as:

::

   cd demo/
   make pdf

Upload PDF to Google Drive
==========================
Set up Google Drive to keep renderer PDF in sync. Follow the steps below:

#. Enable Drive API y download `credentials.json <https://developers.google.com/drive/api/v3/quickstart/python>`_
   by pressing "Enable the Drive API" button.
#. Run ``mkdir -p ~/.config/google-drive/`` and copy *credentials.json* inside *google-drive/* folder.
#. Get folder id from Google Drive url. For example: ``https://drive.google
.com/drive/u/0/folders/1C1FrHclpyNtIX0xVXzlnVxxxxxx``
#. Put this id in the cookiecutter wizard or ``Makefile`` file (``DRIVE_FOLDER`` variable).

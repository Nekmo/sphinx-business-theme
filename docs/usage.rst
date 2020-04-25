
Usage
#####

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

Demo project
============

You can play updating content inside `demo/` dir and making the pdf again as:

::

   cd demo/
   make pdf

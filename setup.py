# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from business_theme import __version__


directory = os.path.dirname(os.path.abspath(__file__))


README_PATH = os.path.join(directory, 'README.rst')


setup(
    name='sphinx-business-theme',
    version=__version__,
    url='https://github.com/Nekmo/sphinx-business-theme',
    license='MIT',
    author='Nekmo',
    author_email='contacto@nekmo.com',
    description='A theme for Sphinx to generate PDF documentation',
    long_description=open(README_PATH, encoding='utf-8').read(),
    zip_safe=False,
    packages=['business_theme'],
    package_data={'business_theme': [
        'theme.conf',
        '*.html',
        'static/styles/*.css',
        'static/js/*.js',
        'static/fonts/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'business_theme = business_theme',
        ],
        'console_scripts': [
            'create-docs = business_theme.__main__:create',
        ]
    },
    install_requires=[
        'sphinx',
        'weasyprint',
        'click',
        'cookiecutter',
        'google-api-python-client',
        'google-auth',
        'google-auth-oauthlib',
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)

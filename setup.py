#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'pipsearch'
DESCRIPTION = 'a library to search through libraries of python 2 and 3 in pipy.'
URL = 'https://github.com/shubhodeep9/pipsearch'
EMAIL = 'Shubhodeep Mukherjee'
AUTHOR = 'shubhodeep9@gmail.com'

# What packages are required for this module to be executed?
REQUIRED = [
    'beautifulsoup4',
    'requests',
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# This will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    extras_require={
        'dev': [
            'flake8',
            'pytest',
            'pytest-cov',
            'pytest-xdist',
            'twine',
            'wheel',
        ]
    },
    include_package_data=True,
    license='Apache-2.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    test_suite='tests',
)

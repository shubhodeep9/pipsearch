#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from pipsearch import __version__

# Package meta-data.
NAME = 'pipsearch'
DESCRIPTION = 'A library to search through libraries of python 2 and 3 in pipy.'
URL = 'https://github.com/shubhodeep9/pipsearch'
EMAIL = 'Shubhodeep Mukherjee'
AUTHOR = 'shubhodeep9@gmail.com'

# What packages are required for this module to be executed?
REQUIRED = [
    'beautifulsoup4',
    'requests',
]

# Import the README and use it as the long-description.
# This will only work if 'README.rst' is present in your MANIFEST.in file!
with open('README.md', encoding='utf-8') as f:
    long_description = '\n' + f.read()


# Where the magic happens:
setup(
    name=NAME,
    version=__version__,
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
    entry_points={
        'console_scripts': [
            'pipsearch=pipsearch.cli:main',
        ],
    },
)

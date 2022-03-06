#! /usr/bin/python
"""This is the main script containing function definitons for scraping
relevant PyPI data."""
from __future__ import absolute_import, division, print_function

import re
import requests

from bs4 import BeautifulSoup


def search(term, limit=None):
    """Search a package in the pypi repositories

    `Arguments:`

    **term** -- the term to search in the pypi repositories

    **limit** -- the maximum amount of results to find
    """

    # Constructing a search URL and sending the request
    url = "https://pypi.org/search/?q=" + term
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')
    packagestable = soup.find('ul', {'class': 'unstyled'})

    # If no package exists then there is no table displayed hence soup.table will be None
    if packagestable is None:
        return []

    packagerows = packagestable.findAll('li')

    # Constructing the result list
    packages = []

    for package in packagerows[:limit]:
        packagedatatd = package.find_all('td')
        packagedata = {
            'name': package.find('span', {'class': 'package-snippet__name'}).text,
            'link': 'https://pypi.org' + package.a['href'],
            'description': package.find('p', {'class': 'package-snippet__description'}).text,
            'version': package.find('span', {'class': 'package-snippet__version'}).text,
        }
        packages.append(packagedata)

    # returning the result list back
    return packages

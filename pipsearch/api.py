#! /usr/bin/python
"""This is the main script containing function definitons for scraping
relevant PyPI data."""
from __future__ import absolute_import, division, print_function
import re
import requests

from bs4 import BeautifulSoup
import click

@click.command()
@click.option('--term', default='', help='Term to search?')
def search(term, limit=None):
    """Search a package in the pypi repositories

    `Arguments:`

    **term** -- the term to search in the pypi repositories

    **limit** -- the maximum amount of results to find
    """

    # Constructing a search URL and sending the request

    # Concatinating the results from splitting will lead to good results
    packages = []
    for each_term in term.split():
        url = "https://pypi.python.org/pypi?:action=search&term=" + each_term
        req = requests.get(url)

        soup = BeautifulSoup(req.text, 'html.parser')
        packagestable = soup.table

        # If no package exists then there is no table displayed hence soup.table will be None
        if packagestable is None:
            continue

        packagerows = packagestable.find_all('tr', {'class': re.compile('[odd|even]')})

        # Constructing the result list

        for package in packagerows[:limit]:
            packagedatatd = package.find_all('td')
            packagedata = {
                'name': packagedatatd[0].text.replace(u'\xa0', ' '),
                'link': 'https://pypi.python.org' + packagedatatd[0].find('a')['href'],
                'weight': int(packagedatatd[1].text),
                'description': packagedatatd[2].text
            }
            packages.append(packagedata)

    # returning the result list back
    print(packages)
    return packages
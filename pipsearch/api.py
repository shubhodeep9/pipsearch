#! /usr/bin/python
"""This is the main script containing function definitons for scraping
relevant PyPI data."""
from __future__ import absolute_import, division, print_function

import requests
from bs4 import BeautifulSoup


def search(term, limit=None):
    """Search a package in the pypi repositories
    """
    def get_packages(soup):
        nonlocal packagenum

        packagestable = soup.find("ul", {"aria-label": "Search results"})
        packagerows = packagestable.find_all('li')

        # Constructing the result list
        for package in packagerows[:limit]:
            packagedata = {
                'name': package.find(class_="package-snippet__name").text,
                'link': 'https://pypi.org' + package.find('a')['href'],
                'version': package.find(class_="package-snippet__version").text,
                'description': package.find(class_="package-snippet__description").text
            }
            packages.append(packagedata)
            packagenum += 1
            if packagenum == limit:
                return True
        return False

    packages = []
    packagenum = 0

    # Get the page number
    soup = BeautifulSoup(requests.get(
                "https://pypi.org/search",
                params={'q': term}
            ).text,"html.parser")
    pn = int(soup.find_all(class_="button button-group__button")[-2].text)
    get_packages(soup)

    # Constructing a search URL and sending the request
    # Concatinating the results from splitting will lead to good results
    for i in range(2, pn+1):
        soup = BeautifulSoup(requests.get(
                "https://pypi.org/search",
                params={'q': term, 'page': i}
            ).text, 'html.parser')
        # Verify that sufficient packages have been searched
        if get_packages(soup):
            break

    return packages

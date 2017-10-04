#! /usr/bin/python

from __future__ import absolute_import, division, print_function
from bs4 import BeautifulSoup
import requests
import re

def search(term, limit=None):
	"""Search a package in the pypi repositories

	`Arguments:`

	**term** -- the term to search in the pypi repositories
	
	**limit** -- the maximum amount of results to find
	"""

	# Constructing a search URL and sending the request
	url = "https://pypi.python.org/pypi?:action=search&term=" + term
	req = requests.get(url)

	#Parsing the html from the response from pypi
	soup = BeautifulSoup(req.text, 'html.parser')

	packagestable = soup.table
	packagerows = packagestable.find_all('tr', {'class':re.compile('[odd|even]')})

	#Constructing the result list
	packages = []
	
	for package in packagerows[:limit]:
		packagedatatd = package.find_all('td')
		packagedata = {
			'name': packagedatatd[0].text.replace(u'\xa0',' '),
			'link': 'https://pypi.python.org' + packagedatatd[0].find('a')['href'],
			'weight': int(packagedatatd[1].text),
			'description': packagedatatd[2].text
		}
		packages.append(packagedata)
	
	#returning the result list back
	return (packages)
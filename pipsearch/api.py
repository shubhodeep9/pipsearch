#! /usr/bin/python

from __future__ import absolute_import, division, print_function
from bs4 import BeautifulSoup
import requests

def search(term):
	url = "https://pypi.python.org/pypi?:action=search&term=" + term
	req = requests.get(url)

	soup = BeautifulSoup(req.text)

	print(soup.body())
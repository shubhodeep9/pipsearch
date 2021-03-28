#! /usr/bin/python
from __future__ import print_function

import sys
import argparse

from . import api, __version__

def main():
    query, search_limit = parse_options()
    if not query:
        print('Enter a search query.')
        sys.exit(0)

    packages = api.search(query, limit=search_limit)
    if len(packages) == 0:
        print('No packages found for query "{}".'.format(query))
        return
    print('First {} packages found for query "{}":'.format(len(packages), query))
    for package in packages:
        print('  '.join((package['name'], package['version'])), package['description'], package['link'], 
              sep='\n', end='\n\n')

def parse_options():
    parser = argparse.ArgumentParser(description='Search packages from PyPI.')
    parser.add_argument('term', metavar='term', type=str, nargs='+',
                        help='Package name to search')
    parser.add_argument('--limit', type=int, nargs='?', default=None,
                        help='The limit of the packages in the search results')
    parser.add_argument('--version', '-V', action='version', version=__version__)
    if len(sys.argv) < 2:
        sys.argv.append("-h")

    namespace = parser.parse_args(sys.argv[1:])
    limit = namespace.limit
    if limit is not None and limit < 1:
        raise ValueError("Limit should be at least 1")
    query = namespace.term  # exclude the options from the search query
    return query, limit

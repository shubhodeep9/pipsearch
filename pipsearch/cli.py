#! /usr/bin/python
from __future__ import print_function

import sys

from pipsearch import api

LIMIT_COMMAND = '--limit'


def main():
    query, search_limit = parse_options()
    if not query:
        print('Enter a search query.')
        sys.exit(0)

    packages = api.search(query, search_limit)
    if len(packages) == 0:
        print('No packages found for query "{}".'.format(query))
        return
    print('First {} packages found for query "{}":'.format(len(packages), query))
    for package in packages:
        print('\n{}\n{}\n{}\n'.format(package['name'], package['description'], package['link']))


def parse_options():
    # if more options are added, the module `argparse` should probably be used instead of this function.
    limit = 5
    lim_index = len(sys.argv)
    if len(sys.argv) < 2:
        return '', 0

    lowered_args = [thing.lower() for thing in sys.argv]
    if LIMIT_COMMAND in lowered_args:
        lim_index = lowered_args.index(LIMIT_COMMAND)
        try:
            limit = int(sys.argv[lim_index + 1])  # get the word after the command and attempt to convert it to an int
        except (IndexError, ValueError):
            pass
        else:
            limit = max(1, limit)  # limit should be at least 1

    query = ' '.join(sys.argv[1:lim_index])  # exclude the options from the search query
    return query, limit

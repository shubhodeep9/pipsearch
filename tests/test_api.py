def test_search(patch_requests):
    from pipsearch.api import search
    a = search('path', 2)
    expected = [
        {'description': 'A demo app for Morepath with record batching',
         'link': 'https://pypi.python.org/pypi/morepath-batching/0.1',
         'name': 'morepath-batching 0.1', 'weight': 10},
        {'description': 'PATH programming language',
         'link': 'https://pypi.python.org/pypi/path/0.33',
         'name': 'path 0.33', 'weight': 10}
    ]
    assert a == expected

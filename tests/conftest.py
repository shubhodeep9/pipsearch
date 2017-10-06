import os
from pytest import fixture
import requests


def mock_pip_html():
    """canonical html example taken from pypi

    :return: string containing the html document
    """
    data_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(data_dir, 'result_page.html'), 'r') as f:
        return f.read()


# avoid spamming pip with requests, monkeypatch requests such it does not actually perform
# a lookup but is given the mock_pip_html
@fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr("requests.models.Response.text", mock_pip_html())
    monkeypatch.setattr("requests.get", lambda x: requests.Response())

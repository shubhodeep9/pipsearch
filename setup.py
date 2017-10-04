from setuptools import setup

setup(name="pipsearch",
	  version="0.7",
	  description="Search pypi modules",
	  url="https://github.com/biggydbs/pipsearch",
	  author="Rahul Arora",
	  author_email="coderahul94@gmail.com",
	  license='MIT',
	  packages=["pipsearch"],
	  scripts=["bin/api"],
	  install_requires=[],
	  zip_safe=False)
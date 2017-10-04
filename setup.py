from setuptools import setup

setup(name="pipsearch",
	  version="1",
	  description="Search pypi modules",
	  url="https://github.com/biggydbs/pipsearch",
	  author="Hitesh Jain",
	  author_email="jain.hitesh30695@gmail.com",
	  packages=["pipsearch"],
	  scripts=["bin/api"],
	  download_url="https://github.com/biggydbs/pipsearch/archive/1.tar.gz",
	  install_requires=[],
	  zip_safe=False)
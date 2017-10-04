from setuptools import setup

setup(name="pipsearch",
	  version="2.5",
	  description="Search pypi modules",
	  url="https://github.com/biggydbs/pipsearch",
	  author="Hitesh Jain",
	  author_email="jain.hitesh30695@gmail.com",
	  packages=["pipsearch"],
	  download_url="https://github.com/biggydbs/pipsearch/archive/2.tar.gz",
	  install_requires=['Click'],
	  include_package_data=True,
	  entry_points='''
        [console_scripts]
        pipsearch=pipsearch.bin.api:search
    	''',
	  zip_safe=False)
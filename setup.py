#!/usr/bin/python
from setuptools import setup 
setup(
    name='pipsearch',
    version='1.0.0',
    install_requires=['beautifulsoup4==4.4.1','requests==2.18.4'],
    description='A library to search for Python 2 and 3 libraries in PyPi.',
    author='Shubhodeep Mukherjee',
    author_email='shubhodeep9@gmail.com',
    url='https://github.com/shubhodeep9/pipsearch',
    packages=['pipsearch'],
    license='Apache'
 )

#!/usr/bin/env python
import os

from setuptools import setup, find_packages


setup(
    name='place',
    version='0.1',
    description='All thing you need for interaction with the terminal output',
    url='https://github.com/Ublimjo/place',

    author='Ublim',
    author_email='ublimjo@gmail.com',

    keywords='place places screen terminale size column columns width line',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)


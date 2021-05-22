#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

version = os.getenv('RELEASE_VERSION', '0.0.0')

setup(
    name='terrathon',
    description='Lightweight Python wrapper around the Terraform CLI',
    license="Mozilla Public License Version 2.0",
    packages=find_packages(),
    python_requires=">=3.6",
    url='https://github.com/restechnica/terrathon',
    version=version
)

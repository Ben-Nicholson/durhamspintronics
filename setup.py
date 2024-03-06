# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:09:11 2024

@author: Ben Nicholson
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="durhamspintronics",
    version="0.0.4",
    author="Ben Nicholson",
    author_email="ben.nicholson@durham.ac.uk",
    description="A collection of instrument control and analysis tools for the Spintronics group at Durham University.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ben-Nicholson/durhamspintronics",
    packages=setuptools.find_packages(),
    python_requires = '>=3',
    install_requires = [
            'matplotlib',
            'scipy',
            'numpy',
    ],
)

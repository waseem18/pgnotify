#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file.
with open(path.join(here, "README.md")) as f:
    long_description = f.read()

# Get package and author details.
about = {}
with open(path.join(here, "pgnotify", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__license__"],
    packages=[about["__title__"]],
    keywords="postgres listen notify triggers",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
)
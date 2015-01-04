# -*- coding: utf-8 -*-
__author__ = "Michaël Krens"
__copyright__ = "Copyright 2015, SignRequest B.V."
from client.client import VERSION
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SignRequest API python client",
    version=VERSION,
    author="Michaël Krens",
    author_email="michael@signrequest.com",
    description="A python client to use the SignRequest REST api",
    # license="BSD",
    keywords="signrequest sign request",
    # url="http://packages.python.org/an_example_pypi_project",
    packages=['client'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        # "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "requests",
    ],
)

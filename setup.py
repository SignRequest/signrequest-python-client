# -*- coding: utf-8 -*-
__author__ = "Michaël Krens"
__copyright__ = "Copyright 2015, SignRequest B.V."

import os
from setuptools import setup

from signrequest_client import __version__ as version


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# helpfull: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
# distribute using: python setup.py sdist bdist_wheel upload

setup(
    name="signrequest-python-client",
    version=version,
    author="Michaël Krens",
    author_email="michael@signrequest.com",
    description="A python client to use the SignRequest REST api",
    keywords="signrequest sign request",
    url="https://github.com/SignRequest/signrequest-python-client",
    packages=['signrequest_client'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires=[
        "requests",
    ],
)

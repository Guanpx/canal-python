# coding: utf8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="canal-py2",
    version="0.5",
    author="magic",
    author_email="guanpeixiang@foxmail.com",
    description="A canal-cilent for python2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Guanpx/canal-python',
    packages=setuptools.find_packages(),
)

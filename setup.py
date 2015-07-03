#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
from codecs import open


version = ''
with open('koordinates/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

history = ''

setup(
    name='koordinates',
    packages=['koordinates',],
    version=version,
    description='A Python client library for a number of Koordinates web APIs',
    long_description=readme + '\n\n' + history,
    author='Koordinates Limited',
    author_email='support@koordinates.com',
    url='https://github.com/koordinates/python-client',
    download_url = 'https://github.com/koordinates/python-client/tarball/0.1',
    keywords='koordinates api',
    license = 'BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    test_suite = 'nose.collector',
)


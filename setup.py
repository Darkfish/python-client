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
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='koordinates',
    packages=['koordinates',],
    version=version,
    description='A Python client library for a number of Koordinates web APIs',
    long_description=readme,
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
    entry_points = {
        'console_scripts': [
            'koordinates-create-token = koordinates.tokens:console_create',
        ],
    },
    install_requires=[
        'python-dateutil>=2,<3',
        'pytz',
        'requests>=2,<3',
        'six>=1.9,<2',
    ],
    test_suite = 'nose.collector',
    tests_require=[
        'nose>=1.3,<2',
        'responses>=0.3',
        'coverage>=3.7,<4',
    ],
    zip_safe=False,
)


#!/usr/bin/env python

# python3 setup.py install

from distutils.core import setup

from munin import __version__ as version

setup(
    name = 'munin',
    version = version,
    description = 'Framework for building Munin plugins',
    author = 'Samuel Stauffer',
    author_email = 'samuel@descolada.com',
    url = 'http://github.com/samuel/python-munin/tree/master',
    packages = ['munin'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from cms_bootstrap3 import __version__
try:
    from pypandoc import convert
except ImportError:
    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]


setup(
    name='djangocms-bootstrap3',
    version=__version__,
    description='Templates and templatetags to be used with djangoCMS and Bootstrap3.',
    author='Jacob Rief',
    author_email='jacob.rief@gmail.com',
    url='https://github.com/jrief/djangocms-bootstrap3',
    packages=find_packages(),
    install_requires=[],
    license='LICENSE-MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=convert('README.md', 'rst'),
    include_package_data=True,
    zip_safe=False
)

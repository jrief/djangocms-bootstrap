#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages
from cms_bootstrap import __version__


with open('README.md') as fh:
    long_description = fh.read()


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
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
]

setup(
    name='djangocms-bootstrap',
    version=__version__,
    description='Templates and templatetags to be used with django-CMS with Bootstrap3 or Bootstrap4.',
    author='Jacob Rief',
    author_email='jacob.rief@gmail.com',
    url='https://github.com/jrief/djangocms-bootstrap',
    packages=find_packages(),
    install_requires=[
        'django-cms>3.4,<3.7',
    ],
    license='MIT',
    platforms=['OS Independent'],
    keywords=['django-cms', 'bootstrap-3', 'bootstrap-4'],
    classifiers=CLASSIFIERS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False
)

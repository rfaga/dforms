#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='dforms',
    version='0.1',
    description='Django Dynamic Forms',
    author='Roberto Faga',
    author_email='rfaga@usp.br',
    long_description=open('README.md', 'r').read(),
    url='http://github.com/rfaga/dforms',
    packages=[
        'dforms',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

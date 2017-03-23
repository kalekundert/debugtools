#!/usr/bin/env python3
# encoding: utf-8

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as file:
    readme = file.read()

if sys.version_info < (3,):
    dependencies='inform pathlib'
else:
    dependencies='inform'

setup(
    name='debugtools',
    version='0.3.9',
    author='Kale Kundert & Ken Kundert',
    author_email='debugtools@shalmirane.com',
    description='',
    long_description=readme,
    url='https://github.com/kenkundert/debugtools',
    py_modules='debugtools'.split(),
    include_package_data=True,
    install_requires=dependencies.split(),
    license='MIT',
    keywords='debugtools'.split(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
)

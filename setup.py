#!/usr/bin/env python3
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
with open('debugtools/__init__.py') as file:
    version_pattern = re.compile("__version__ = '(.*)'")
    version = version_pattern.search(file.read()).group(1)

with open('README.rst') as file:
    readme = file.read()

setup(
    name='debugtools',
    version=version,
    author='Kale Kundert',
    author_email='kale@thekunderts.net',
    description='',
    long_description=readme,
    url='https://github.com/kalekundert/debugtools',
    packages=[
        'debugtools',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords=[
        'debugtools',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],
)

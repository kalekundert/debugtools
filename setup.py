#!/usr/bin/env python3
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name='debugtools',
    version='0.1.0',
    author='Kale Kundert',
    author_email='kale@thekunderts.net',
    description='',
    long_description=readme,
    url='https://github.com/kalekundert/debugtools',
    pymodules=[
        'debugtools',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    keywords=[
        'debugtools',
    ],
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

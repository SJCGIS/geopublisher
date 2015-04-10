#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [

]

test_requirements = [
    'tox',
    'nose>=1.0',
    'mock>=1.0',
    'coverage==3.7.1'
]

setup(
    name='geopublisher',
    version='0.1.2',
    description="Tools to publish GIS data using Arcpy",
    long_description=readme + '\n\n' + history,
    author="Nick Peihl",
    author_email='nickp@sanjuanco.com',
    url='https://github.com/sjcgis/geopublisher',
    packages=[
        'geopublisher',
    ],
    package_dir={'geopublisher':
                 'geopublisher'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache 2.0",
    zip_safe=False,
    keywords='geopublisher',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Win32 (Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    tests_require=test_requirements
)

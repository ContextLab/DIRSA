# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DIRSA',
    version='0.1.0',
    description='Estimate clustering from dynamic intersubject functional connectivity patterns',
    long_description=readme,
    author='DIRT',
    author_email='me@kennethreitz.com',
    url='https://github.com/ContextLab/DIRSA',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

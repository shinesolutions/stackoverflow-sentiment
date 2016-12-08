# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='so-sentiment',
        version='0.0.1',
        description='Stackoverflow sentiment analysis',
        long_description=readme,
        author='Graham Polley',
        author_email='polleyg@gmail.com',
        url='https://github.com/shinesolutions/stackoverflow-sentiment',
        license=license,
        packages=find_packages(exclude=('tests', 'docs'))
)

"""Installation setup."""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

PACKAGE = 'faker_extras'
VERSION = '1.0.0'


def _get_requires(filepath):
    path = '{}/{}'.format(os.path.abspath(os.path.dirname(__file__)), filepath)
    with open(path) as reqs:
        return [req for req in reqs.read().split('\n') if req]

keywords = ['faker_extras', 'fake data generation', 'faker', 'data generator']
description = ('An extended set of data providers for the Faker library.')
setup(
    name='faker_extras',
    version=VERSION,
    description=description,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    maintainer='Chris Tabor',
    maintainer_email='dxdstudio@gmail.com',
    url='https://github.com/christabor/faker_extras',
    keywords=keywords,
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=_get_requires('requirements.txt'),
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ]
)

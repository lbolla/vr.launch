#!/usr/bin/env python

# Project skeleton maintained at gitlab://support/skeleton
# based on https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

group = 'support'
name = 'vr.launch'
description = 'Facilities for launching apps under Velociraptor'
nspkg_technique = 'managed'
"""
Does this package use "native" namespace packages or
pkg_resources "managed" namespace packages?
"""

params = dict(
    name=name,
    use_scm_version=True,
    author="YouGov, Plc.",
    author_email="open-source@yougov.com",
    description=description or name,
    long_description=long_description,
    url='https://github.com/yougov/{name}'.format(**locals()),
    packages=setuptools.find_packages(),
    include_package_data=True,
    namespace_packages=(
        name.split('.')[:-1] if nspkg_technique == 'managed'
        else []
    ),
    python_requires='>=2.7',
    install_requires=[
        'pyyaml',
        'jaraco.collections!=1.2',
        'six',
    ],
    extras_require={
        'testing': [
            # upstream
            'pytest>=2.8',
            'pytest-sugar>=0.9.1',
            'collective.checkdocs',
            'pytest-flake8',

            # local
        ],
        'docs': [
            # upstream
            'sphinx',
            'jaraco.packaging>=3.2',
            'rst.linker>=1.9',

            # local
        ],
    },
    setup_requires=[
        'setuptools_scm>=1.15.0',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
    },
)
if __name__ == '__main__':
    setuptools.setup(**params)

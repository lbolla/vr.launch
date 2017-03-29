#!/usr/bin/env python

# Project skeleton maintained at kiln://support/skeleton
# based on https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

group = ''
name = 'skeleton'
dashname = name.replace('.', '-')
description = ''
url_tmpl = 'https://yougov.kilnhg.com/Code/Repositories/{group}/{dashname}'

params = dict(
    name=name,
    use_scm_version=True,
    author="YouGov, Plc.",
    author_email="dev@yougov.com",
    description=description or name,
    long_description=long_description,
    url=url_tmpl.format(**locals()),
    packages=setuptools.find_packages(),
    include_package_data=True,
    namespace_packages=name.split('.')[:-1],
    python_requires='>=2.7',
    install_requires=[
    ],
    extras_require={
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

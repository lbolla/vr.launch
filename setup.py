#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

setup_params = dict(
	name='yg.launch',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	url="https://yougov.kilnhg.com/Code/Repositories/support/yg-launch",
	packages=setuptools.find_packages(),
	namespace_packages=['yg'],
	zip_safe=False,
	install_requires=[
		'pyyaml',
		'jaraco.collections',
		'six',
	],
	setup_requires=[
		'hgtools',
		'pytest-runner',
	],
	tests_require=[
		'pytest',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)

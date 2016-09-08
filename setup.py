#!/usr/bin/env python

from setuptools import find_packages, setup

# setup the project
setup(
    name='cmsplugin-forms-builder',
    version='1.1.0',
    description='django-cms plugin for cmsplugin-forms-builder',
    long_description=open('README.md').read(),
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='https://github.com/nimbis/cmsplugin-forms-builder/',
    packages=find_packages(exclude=["tests", ]),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    install_requires=[
        'Django',
        'django-cms>=3.3.1',
        'django-forms-builder',
    ],
    zip_safe=False
)

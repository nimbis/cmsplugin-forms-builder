#!/usr/bin/env python

from setuptools import find_packages, setup
from pip.req import parse_requirements
from uuid import uuid1


# parse requirements
reqs = parse_requirements("requirements/common.txt", session=uuid1())

# setup the project
setup(
    name='cmsplugin-forms-builder',
    version='0.1.11',
    description='django-cms plugin for cmsplugin-forms-builder',
    long_description=open('README.rst').read(),
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
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False
)

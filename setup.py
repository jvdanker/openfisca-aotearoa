#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Aotearoa',
    version='9.1.0',
    author='New Zealand Government, Service Innovation Lab',
    author_email='brenda.wallace@dia.govt.nz',
    description=u'OpenFisca tax and benefit system for Aotearoa',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/ServiceInnovationLab/openfisca-aotearoa',
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 24.3.0, < 25.0',
        ],
    extras_require={
        'test': [
            'flake8 >=3.4.0,<3.7.0',
            'flake8-print',
            'nose',
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )

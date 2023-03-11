#!/usr/bin/env python3

import setuptools

install_requires = [
        ]

setuptools.setup(
    name="allagan",
    python_requires=">=3.9.10",
    description="A simple macro tool for FFXIV",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'allagan = src:main',
        ],
    },
    include_package_data=True,
    )
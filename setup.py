#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='perler_beads',
    version='0.1',
    url='https://github.com/Everley1993/PerlerBeads',
    description='PerlerBeads',
    license='MIT',
    author='Everley',
    author_email='463785757@qq.com',
    platforms=['any'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'perler_beads= perler_beads.main:main',
        ],
    },
    install_requires=['Pillow'],
    include_package_data=True,
)

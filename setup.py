#!/usr/bin/env python3

from setuptools import setup

modname = distname = 'iwtools'

setup(
    name=distname,
    py_modules=['iwtools','module'],
    version='0.0.1',
    description='Tool for real-time monitoring of wireless network devices.',
    author='Wander Vilhalva Domingos',
    author_email='wandervilhalvadomingos@gmail.com',
    install_requires=['setuptools'],
    entry_points='''
    [console_scripts]
    iwtools=iwtools:main
    '''
)
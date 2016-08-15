# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="mailroom",
    description="The mailroom implementation tracks donations and send thank you letters.",
    version='0.1.1',
    author="Zach Rickert, Steven Than, David Smith",
    author_email="zachrickert@gmail.com, steventhan11@gmail.com, dbsmith.dbs83@gmail.com",
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
    entry_points={'console_scripts': ["mailroom = mailroom:main_menu"]}
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: setup.py.py
# @Time: 2019/8/23 14:07


import io
import re

from setuptools import setup, find_packages

with io.open("README.rst", "rt", encoding="utf8") as f:
        readme = f.read()

with io.open("src/flask/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='casearch',
    version=version,
    author='TnTomato',
    author_email='474093103@qq.com',
    description='Retrieve from ElasticSearch',
    long_description=readme,
    url='https://github.com/EathonTnT/casearch',
    license='MIT',
    packages=find_packages(exclude='test'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'elasticsearch>=6.3.0',
        'elasticsearch_dsl>=6.3.0'
    ]
)

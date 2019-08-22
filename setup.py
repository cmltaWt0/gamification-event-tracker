#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os
import re

from setuptools import setup, find_packages


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='gamification-event-tracker',
    version=get_version('gamification_event_tracker', '__init__.py'),
    description="""
        Process to watch edX tracking logs and convert/publish
        them as RaccoonGang gamification service.
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Max K',
    author_email='cmltaWt0@gmail.com',
    url='https://github.com/cmltaWt0/gamification-event-tracker',
    packages=find_packages(),
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='Gamma Gamification Raccoongang',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup

__author__ = "Igor R. Dejanovic <igor.dejanovic AT gmail DOT com>"
__version__ = "0.1"

GITHUB_ACCOUNT = 'TODO'
NAME = 'textx-gen-er-flask'
DESC = 'er_flask textX generator'
VERSION = __version__
AUTHOR = __author__.split('<')[0].strip()
AUTHOR_EMAIL = __author__
LICENSE = 'MIT'
URL = 'https://github.com/%s/%s' % (GITHUB_ACCOUNT, NAME)
DOWNLOAD_URL = 'https://github.com/%s/%s/archive/v%s.tar.gz' % \
    (GITHUB_ACCOUNT, NAME, VERSION)
README = codecs.open(os.path.join(os.path.dirname(__file__), 'README.md'),
                     'r', encoding='utf-8').read()

setup(
    name = NAME,
    version = VERSION,
    description = DESC,
    long_description = README,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    maintainer = AUTHOR,
    maintainer_email = AUTHOR_EMAIL,
    license = LICENSE,
    url = URL,
    download_url = DOWNLOAD_URL,
    packages = ["er_flask"],
    include_package_data=True,
    install_requires = ["textx-tools", "textx-lang-er", "Jinja2"],
    keywords = "tools generator language DSL",
    entry_points={
        'textx_gen': [
            'er_flask = er_flask.gen:gendesc',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]

)

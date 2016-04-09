# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'usermanagement'
VERSION = '0.0.1'


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="A simple usermanagement system which controls the application based on user roles",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Aladdin Free Public License (AFPL)",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords="management usermanagement permission",
    author="FeLiX StEpHeN",
    author_email="felsen88@gmail.com",
    url="https://github.com/felsen/usermgmt",
    license="MIT",
    include_package_data=False,
    package_data={
        '': ['README.rst', 'requirements.txt', ],
        },
    install_requires=readlist('requirements.txt'),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)

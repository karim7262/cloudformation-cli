#!/usr/bin/env python
import os.path
import re

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(HERE, *parts), "r", encoding="utf-8") as fp:
        return fp.read()


# https://packaging.python.org/guides/single-sourcing-package-version/
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="uluru-cli",
    version=find_version("uluru", "__init__.py"),
    description=__doc__,
    long_description=read("README.rst"),
    author="Amazon Web Services",
    url="https://aws.amazon.com/cloudformation/",
    packages=find_packages(exclude=["tests*"]),
    # package_data -> use MANIFEST.in instead
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "jinja2",  # fmt: off
        "jsonschema",  # fmt: off
        "pyyaml",  # fmt: off
    ],
    entry_points={"console_scripts": ["uluru-cli = uluru.cli:main"]},
    license="Apache License 2.0",
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ),
    keywords="Amazon Web Services AWS CloudFormation",
)
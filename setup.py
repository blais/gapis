#!/usr/bin/env python3
"""Setup file for gapis."""

import setuptools

setuptools.setup(
    name="gapis",
    version='1.0',
    description="Auth Files Management for Locals Scripts for Google Apis.",
    long_description=
    """
    This is intended to be imported to get credentials, that given a script name,
    will know where to find the secrets and automatically cache the credentials so
    we can easily run command-line scripts with cached credentials to the various
    Google APIs.
    """,
    license="Apache 2.0",
    author="Martin Blais",
    author_email="blais@furius.ca",
    url="https://github.com/blais/gapis",
    download_url="https://github.com/blais/gapis",
    packages=setuptools.find_packages(),
    install_requires = ['google-auth'],
    python_requires='>=3.8',
)

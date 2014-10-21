from setuptools import setup


def get_version(filename):
    """
    Parse the value of the __version__ var from a Python source file
    without running/importing the file.
    """
    import re
    version_pattern = r"^ *__version__ *= *['\"](\d+\.\d+\.\d+)['\"] *$"
    match = re.search(version_pattern, open(filename).read(), re.MULTILINE)

    assert match, ("No version found in file: {!r} matching pattern: {!r}"
                   .format(filename, version_pattern))

    return match.group(1)

def install_requires():
    deps = ["six >= 1.0.0, < 2.0.0"]

    # Install ordereddict if an implementation is not in collections
    # (Py <= 2.6).
    try:
        from collections import OrderedDict
    except ImportError:
        deps.append("ordereddict")

    return deps


def tests_require():
    deps = ["mock >= 1.0.0, < 2.0.0", "pytz"]

    # Add unittest2 to tests_require if needed
    import unittest
    if not hasattr(unittest.TestCase, "assertIsNone"):
        deps.append("unittest2")

    import logging.config
    if not hasattr(logging.config, "dictConfig"):
        deps.append("logutils")

    return deps


setup(
    name="jsonlogging",
    description="jsonlogging provides structured log output from the "
                "logging module in JSON format",
    author="Hal Blackburn",
    author_email="hwtb2@cam.ac.uk",
    url="https://github.com/h4l/jsonlogging",
    version=get_version("jsonlogging/__init__.py"),
    packages=["jsonlogging"],
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: System :: Logging"
    ],
    long_description=open("README.md").read(),
    install_requires=install_requires(),
    test_suite="jsonlogging.tests.test_all",
    tests_require=tests_require()
)

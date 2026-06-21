from irelease.irelease import(
    make_script,
    run,
    main)

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.3.3'


# module level doc-string
__doc__ = """
irelease - A Python package to automate releasing your package to PyPI and GitHub
==================================================================================

**irelease**

Overview
--------
irelease streamlines the process of releasing your Python package by automating versioning, building, tagging, and publishing to PyPI and GitHub.

Usage
-----
1. Navigate to the root directory of your package (where `pyproject.toml` or `setup.py` is located).
2. Run the following command to start the release process:
>>> pyrelease

To see all available options and arguments:
>>> pyrelease --help

Features
--------
- Automatically bumps version numbers.
- Builds source and wheel distributions.
- Publishes releases to PyPI.
- Optionally creates GitHub tags and releases.
- Cleans build artifacts.

References
----------
* https://github.com/erdogant/irelease

"""

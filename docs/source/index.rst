irelease's documentation!
=========================

|python| |pypi| |docs| |stars| |LOC| |downloads_month| |downloads_total| |license| |forks| |open issues| |project status| |DOI| |repo-size|

-----------------------------------

*irelease* — Python library by erdogant.


iRelease is an interactive release tool that automates GitHub and PyPI publishing for Python projects. It provides a minimal entry point that forwards command‑line arguments to the core logic, keeping the public API small while exposing powerful functions such as `github_version` to fetch the latest tag, `get_pypi_credentials` to retrieve credentials securely, `make_script` to generate reusable bash scripts, and `run` to perform the full release workflow. The library’s CLI is built with clizard, offering an intuitive interface for creating releases, building distribution packages, and pushing tags without manual scripting. By encapsulating common release steps—version detection, credential handling, package build, Git tagging, and PyPI upload—iRelease reduces boilerplate, eliminates errors, and speeds up continuous delivery pipelines for Python developers.


.. code-block:: console

   pip install irelease

-----------------------------------


Content
=======

.. toctree::
   :maxdepth: 1
   :caption: Installation

   Installation


.. toctree::
   :maxdepth: 1
   :caption: Summary

   Summary


.. toctree::
   :maxdepth: 1
   :caption: Examples

   Examples



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |python| image:: https://img.shields.io/pypi/pyversions/irelease.svg
    :alt: Python
    :target: https://erdogant.github.io/irelease/

.. |pypi| image:: https://img.shields.io/pypi/v/irelease.svg
    :alt: PyPI version
    :target: https://pypi.org/project/irelease/

.. |docs| image:: https://img.shields.io/badge/Sphinx-Docs-blue.svg
    :alt: Sphinx documentation
    :target: https://erdogant.github.io/irelease/

.. |stars| image:: https://img.shields.io/github/stars/erdogant/irelease
    :alt: Stars
    :target: https://github.com/erdogant/irelease

.. |LOC| image:: https://sloc.xyz/github/erdogant/irelease/?category=code
    :alt: lines of code
    :target: https://github.com/erdogant/irelease

.. |downloads_month| image:: https://static.pepy.tech/personalized-badge/irelease?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month
    :alt: Downloads per month
    :target: https://pepy.tech/project/irelease

.. |downloads_total| image:: https://static.pepy.tech/personalized-badge/irelease?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
    :alt: Downloads in total
    :target: https://pepy.tech/project/irelease

.. |license| image:: https://img.shields.io/badge/license-MIT-green.svg
    :alt: License
    :target: https://github.com/erdogant/irelease/blob/master/LICENSE

.. |forks| image:: https://img.shields.io/github/forks/erdogant/irelease.svg
    :alt: Github Forks
    :target: https://github.com/erdogant/irelease/network

.. |open issues| image:: https://img.shields.io/github/issues/erdogant/irelease.svg
    :alt: Open Issues
    :target: https://github.com/erdogant/irelease/issues

.. |project status| image:: http://www.repostatus.org/badges/latest/active.svg
    :alt: Project Status
    :target: http://www.repostatus.org/#active

.. |DOI| image:: https://zenodo.org/badge/246504758.svg
    :alt: Cite
    :target: https://zenodo.org/badge/latestdoi/246504758

.. |repo-size| image:: https://img.shields.io/github/repo-size/erdogant/irelease
    :alt: repo-size
    :target: https://github.com/erdogant/irelease


.. include:: add_bottom.add

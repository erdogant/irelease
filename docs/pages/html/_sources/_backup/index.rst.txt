irelease's documentation!
=========================

|python| |pypi| |docs| |stars| |LOC| |downloads_month| |downloads_total| |license| |forks| |open issues| |project status| |DOI| |repo-size|

-----------------------------------

*irelease* — Python library by erdogant.


iRelease automates the entire Python package release cycle, from determining the latest GitHub tag to publishing on PyPI with a single command. It introspects your project’s `irelease.py` module, generates a ready‑to‑run Bash script (`make_script`) and CLI wrapper via clizard, and handles credential retrieval (`get_pypi_credentials`). The library streamlines version bumping, changelog creation, Git tagging, and PyPI upload, ensuring every release follows the same reproducible workflow. By eliminating manual steps and boilerplate code, iRelease reduces human error, speeds up deployment, and keeps your distribution process consistent across projects. It is ideal for developers who need a reliable, repeatable release pipeline without writing custom scripts or managing complex CI configurations.


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


.. toctree::
   :maxdepth: 1
   :caption: FAQ

   FAQ


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
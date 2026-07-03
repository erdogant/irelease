Background
##################

The pythyon pypi release library is designed to easily release your own library at pypi.
At its core, the library exposes a minimal package entry point which acts as a thin wrapper that forwards command‑line arguments to the underlying logic implemented in :mod:`irelease`.

The CLI layer is automatically generated from the user’s project structure and configuration files. It parses shell arguments, loads optional metadata such as ``.clizard`` or ``.pypirc``, applies any overrides provided at runtime, and then delegates execution to the release logic in :mod:`irelease`. This design eliminates repetitive coding of argument parsers and configuration loaders, reducing human error during packaging and ensuring that every release follows a consistent set of steps.


Output
-------

Running irelease produces a fully packaged distribution ready for upload to PyPI or any other package index.
The generated artifacts include wheel files, source distributions, and optionally documentation archives.
In addition to building these artifacts, the library can perform pre‑release checks such as linting, unit testing, and static analysis, ensuring that only code meeting quality standards is released.

The output of a typical release run is a concise summary printed to the console:

.. code-block:: text

   ✔  Linting passed
   ✔  Tests passed (42)
   📦  Built wheel: myproject-1.0.0-py3-none-any.whl
   📦  Built sdist: myproject-1.0.0.tar.gz
   🚀  Uploaded to PyPI

This summary gives developers immediate feedback on the success of each step and highlights any failures that require attention before a new version can be published.

Schematic Overview
####################################

The high‑level workflow of irelease is illustrated below. The diagram shows how user input, configuration files, and internal logic interact to produce a release artifact.

.. code-block:: text

            +--------------------+
            |  Release Logic     |
            |  (irelease.py)     |
            +---------+----------+
                      |
                      v
          +---------------------------+
          |  Build Artifacts & Tests  |
          +------------+--------------+
                       |
                       v
              +-------------------+
              |  Upload to PyPI   |
              +-------------------+

The diagram demonstrates that the CLI merely translates user intent into concrete calls, while all heavy lifting—validation, building, testing, and uploading—is handled by the core release logic. This separation of concerns keeps the interface simple yet powerful.

.. include:: add_bottom.add

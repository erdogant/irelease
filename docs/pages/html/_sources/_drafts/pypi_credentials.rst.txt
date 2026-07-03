pypi_credentials
#################

Retrieving PyPI Credentials
==========================

Programmatically obtaining credentials for uploading packages to the Python Package Index (PyPI) is a foundational capability in any automated release pipeline. When developers manually type usernames and passwords into scripts or CI configuration files, they expose sensitive information to version control systems, logs, and potentially insecure network channels. By centralizing credential management in the standard ``~/.pypirc`` file, teams can keep secrets out of source code while still enabling reproducible builds across local machines, continuous integration agents, and deployment servers.

The :func:`irelease.get_pypi_credentials` helper abstracts away the intricacies of locating and parsing this configuration file. It is intentionally lightweight: it relies solely on Python’s built‑in :mod:`configparser` module and the operating system’s file paths, avoiding external dependencies that could complicate environment setup or introduce version drift. This design choice aligns with the principle of least surprise—developers can drop the function into any script without worrying about additional package installations.

When invoked, ``get_pypi_credentials`` reads a ``.pypirc`` file directly from the current working directory (or falls back to the user’s home directory if it cannot be found). Once located, the file is parsed using :class:`configparser.ConfigParser`, which gracefully handles INI‑style syntax, comments, and whitespace normalization. If the required ``[pypi]`` section or its ``username``/``password`` fields are missing, the function returns ``(None, None)`` and prints a message when the verbosity level is 3 or higher.

The function’s single parameter, ``verbose``, controls diagnostic output. At a default value of **0**, it suppresses all messages; setting it to **3** or higher will print a helpful message indicating that no credentials were found. Lower verbosity levels keep the function silent, making it suitable for non‑interactive scripts where accidental prompts would cause failures.

.. list-table:: Parameters for :func:`irelease.get_pypi_credentials`
   :widths: 15 10 75
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``verbose``
     - int
     - Controls diagnostic verbosity; prints a message when >= 3. (default=0)

.. code-block:: python

    from irelease import get_pypi_credentials

    username, password = get_pypi_credentials(verbose=3)
    if username is None:
        raise RuntimeError("PyPI credentials not found.")

Important Notes
---------------

The ``.pypirc`` file must follow the standard format so that :func:`get_pypi_credentials` can locate and parse it correctly. A minimal example looks like this:

.. code-block:: text

    [distutils]
    index-servers=pypi

    [pypi]
    username=your_username
    password=your_password

Backend Notes
-------------

The :func:`irelease.get_pypi_credentials` function is used internally by irelease when uploading to PyPI via twine. It abstracts away file parsing and provides a simple tuple interface for the rest of the package.

.. include:: add_bottom.add
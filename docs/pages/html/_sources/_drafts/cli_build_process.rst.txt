cli_build_process
##################

Package Entry Point (__init__.py)
================================

The core of the release automation is exposed through a lightweight package entry point defined in ``__init__.py``.  
This module serves as the bridge between the user‑facing command line and the underlying logic implemented in *irelease.py*.  
By keeping the public surface minimal, developers can focus on extending or customizing the workflow without being overwhelmed by boilerplate code.

The primary functions – ``make_script``, ``run`` and ``main`` – are intentionally simple wrappers.  They exist to provide a clear separation of concerns: generating the shell wrapper, executing the release pipeline, and orchestrating the command‑line interface respectively.  
This design choice ensures that each function can be unit‑tested in isolation while still offering a cohesive experience when invoked from the terminal.

Metadata such as ``__author__``, ``__email__`` and ``__version__`` are declared at module level to aid introspection tools and to satisfy packaging conventions.  The module imports the core logic from *irelease.py* and registers the CLI entry point through a small helper that patches ``sys.argv`` for command‑line emulation.

.. code-block:: python

   >>> pyrelease
   >>> pyrelease --help


Basic Usage Examples (examples.py)
=================================

The ``examples.py`` script demonstrates how to invoke the release automation from within Python scripts or interactive sessions.  
By calling ``irelease.run()`` directly, users can trigger the full build, test, and publish cycle without leaving the interpreter.  
This approach is especially useful for continuous‑integration pipelines where a programmatic interface is preferred over shell commands.

Running ``irelease.run()`` with no arguments executes the default release script that ships with the package.  The function accepts several keyword arguments that allow fine‑grained control over the workflow, such as specifying the author name, choosing a particular script type (e.g., ``'pca'``), toggling cleanup or installation steps, providing Twine configuration, and adjusting verbosity.

The following example shows both a default invocation and a customized run:

.. code-block:: python

   import irelease
   print(irelease.__version__)
   irelease.run()
   # Run a specific script
   irelease.run('erdogant','pca',clean=False,install=False,twine=None,verbose=3)

Parameter Table for ``irelease.run``
-----------------------------------

.. list-table:: Parameters of irelease.run
   :widths: 20 15 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - name
     - str
     - Author/username identifier
   * - script_type
     - str
     - Type of script to run (e.g., 'pca')
   * - clean
     - bool
     - Whether to clean up after execution
   * - install
     - bool
     - Whether to install dependencies
   * - twine
     - any
     - Twine configuration object
   * - verbose
     - int
     - Verbosity level

Important Notes
===============

The package is MIT licensed and authored by Erdogan Tasksen.  
``get_pypi_credentials()`` reads credentials from a ``.pypirc`` file in the current working directory, enabling secure uploads to PyPI without hard‑coding secrets.  
``make_script()`` generates a POSIX‑compatible ``release.sh`` wrapper and copies the source to ``release.py``, allowing users to execute the release process with a single shell command.  
Clizard auto‑generates an interactive CLI that wraps ``irelease.main()``, providing both ``argv``‑style and keyword‑style invocation, thereby simplifying user interaction while preserving full flexibility.

Backend Notes
-------------

The core module relies on standard libraries such as ``configparser``, ``shutil`` and ``os``, and third‑party packages including ``numpy``, ``packaging``, ``webbrowser`` and ``toml``.  
File system side effects include the creation of ``release.sh`` and ``release.py`` in the current working directory.  
The clizard wrapper temporarily patches ``sys.argv`` to emulate command‑line execution, ensuring that the same code path is exercised whether invoked from a script or an interactive session.

.. include:: add_bottom.add
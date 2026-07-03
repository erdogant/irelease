The *irelease* package offers a concise API that automates the most common tasks involved in publishing Python projects.  This page walks through several representative use cases, explains why each parameter matters in real‑world release workflows, and provides runnable code snippets that can be dropped straight into a Python REPL or script.

Basic Run
##################

The simplest way to trigger a release is to call `irelease` or `pyrelease` with no arguments.
This default invocation relies on module‑level configuration discovered from the current working directory.
By inspecting files such as ``setup.py`` or ``pyproject.toml`` it automatically determines the project name, version, and author information.
The function then performs a minimal set of actions: it builds source and wheel distributions, uploads them to PyPI using the locally configured credentials, and creates a corresponding GitHub release tag if a remote repository is detected.

.. code-block:: bash
    >>> pyrelease
    >>> irelease

Run with Parameters
####################################

Often users need finer control over the release process.  The `irelease` function accepts several optional keyword arguments that let you override the automatic discovery logic, toggle cleaning and installation steps, or supply custom Twine configuration.  Specifying these options is particularly useful when working on multiple projects in a single environment or when integrating with external CI services that provide their own authentication mechanisms.

Parameters of `irelease`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Parameters of irelease.run
   :widths: 20 15 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - name
     - str
     - Author/username identifier used for tagging and release metadata.
   * - script_type
     - str
     - Type of script to run (e.g., ``'pca'``) – determines which internal workflow is invoked.
   * - clean
     - bool
     - Whether to remove existing build artifacts before starting a new build cycle. ``True`` guarantees a fresh environment; ``False`` preserves intermediate files for debugging.
   * - install
     - bool
     - Controls whether the freshly built wheel should be installed into the current Python environment.  Handy when you want to test the release immediately after upload.
   * - twine
     - any
     - Path or configuration object passed directly to Twine. ``None`` uses the default ``~/.pypirc`` settings.
   * - verbose
     - int
     - Verbosity level for logging; higher values emit more detailed progress information useful during troubleshooting.

A typical invocation that disables cleaning and installation while enabling verbose output might look like this:

.. code-block:: bash
    >>> irelease --help
    >>> irelease --u erdogant


Retrieve PyPI Credentials
####################################

pyrlease can automatically reads authentication details from a local ``.pypirc`` configuration file, which is the standard location for Twine to find your PyPI username and password or API token.
The function returns a tuple ``(username, password)`` if both keys are present in the ``[pypi]`` section; otherwise it falls back to ``(None, None)``.  When the optional ``verbose`` flag is set to a value of three or higher, the function prints diagnostic information and prompts the user to provide missing credentials interactively.

.. code-block:: bash
    >>> irelease --help
    >>> irelease --t .pypirc

.. include:: add_bottom.add

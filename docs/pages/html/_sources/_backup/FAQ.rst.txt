FAQ
====

Installation and Setup
----------------------
The *irelease* package is distributed through PyPI, making it straightforward to add to any Python environment. A single command installs the library and its minimal dependencies:

.. code-block:: console

   pip install irelease

Once installed, the next step is to provide your GitHub credentials so that releases can be uploaded automatically. The helper function :func:`make_script` copies *irelease.py* into the working directory, simplifying subsequent releases by providing a lightweight shell wrapper. This design keeps sensitive information out of the source tree while still enabling fully automated publishing.

The package expects a **pyproject.toml** or **setup.py** in the project root to discover metadata such as name, version, and dependencies. Without this file *irelease* cannot locate the distribution artifacts it needs to build and publish. Therefore, before running any release commands you should verify that your repository contains one of these configuration files.

The command line interface is intentionally lightweight: ``python -m irelease --help`` lists all available subcommands and options. This single entry point eliminates the need for a separate script or wrapper, reducing maintenance overhead and keeping the user experience consistent across platforms.

A typical setup sequence looks like this:

.. code-block:: python

   # Generate a release script
   make_script()

   # Run a full release (build, tag, upload)
   run(username="erdogant", packagename="irelease")

Parameter table for :func:`make_script` and :func:`run`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Parameter
     - Type
     - Description
   * - username
     - str
     - GitHub account name used when creating tags/releases.
   * - packagename
     - str
     - Name of the package to be released; must match repository and distribution names.
   * - clean
     - bool
     - If True, removes local build artifacts before creating a new release.
   * - twine
     - str
     - Path to the twine executable used for uploading distributions to PyPI.
   * - verbose
     - int
     - Verbosity level; higher values print more detailed progress messages.

Common Errors and Troubleshooting
---------------------------------
Typical errors when using *irelease* arise from missing credentials in ``~/.pypirc``, incorrect package names, or network failures during upload. The :func:`run` function accepts a ``verbose`` flag that can be increased to 4 for more diagnostics. Ensuring that the GitHub account has permission to create tags and releases is essential; otherwise the tagging step will fail silently.

Another frequent pitfall is attempting to run *irelease* in a directory without a valid packaging configuration. Because the tool relies on ``pyproject.toml`` or ``setup.py`` for metadata, its absence leads to ambiguous build failures that can be hard to trace. Running ``python -m irelease --check`` (if available) before a full release can surface such issues early.

When network errors occur during upload, retrying the command often resolves transient problems. However, persistent timeouts may indicate firewall restrictions or incorrect proxy settings; configuring environment variables like ``HTTP_PROXY`` and ``HTTPS_PROXY`` can mitigate these situations.

Example of increasing verbosity for debugging:

.. code-block:: python

   # Increase verbosity for debugging
   run(username="erdogant", packagename="irelease", verbose=4)

Parameter Choices
-----------------
The :func:`run` function offers several optional parameters that allow users to tailor the release process to their workflow. Setting ``clean=True`` ensures that stale distribution files are removed before building, which can prevent accidental uploads of outdated artifacts. Specifying a custom path for ``twine`` is useful when the executable resides in a non-standard location or when using a virtual environment that does not expose it globally.

If you only want to create GitHub releases without uploading to PyPI, set ``--pypi False``. Conversely, use ``--github False`` to skip GitHub tagging when publishing locally. These flags give fine-grained control over which parts of the release pipeline are executed.

Example: Release only to PyPI

.. code-block:: python

   # Release only to PyPI
   run(username="erdogant", packagename="irelease", github=False)

Performance Tips
----------------
Running :func:`make_script` once creates a lightweight shell wrapper that avoids repeated Python imports, thereby reducing startup time for subsequent releases. The ``--clean`` flag should be used sparingly; cleaning large build directories can add overhead and may not be necessary if your CI pipeline already handles artifact cleanup.

For continuous integration pipelines, caching the ``~/.pypirc`` file and GitHub tokens can dramatically reduce authentication time. Storing these secrets in environment variables or secure storage solutions ensures that each job starts with the required credentials without manual intervention.

Limitations
-----------
The :func:`github_version` function only retrieves the latest tag from the default branch; it does not support pre-releases or custom tag prefixes. The package assumes a standard Python packaging layout and may fail with non-standard project structures, such as those that use unconventional directory hierarchies or build systems.

Comparison to Alternatives
--------------------------
Unlike full-featured CI/CD solutions, *irelease* focuses on simplicity: it automates version bumping, building wheels, tagging GitHub releases, and uploading to PyPI in a single command. It does not provide advanced workflow orchestration or multi-environment deployment features found in tools like ``setuptools_scm`` or ``twine-multi``.

.. include:: add_bottom.add
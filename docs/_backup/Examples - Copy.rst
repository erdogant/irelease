Examples
#########

The *irelease* library is designed to streamline the release process of Python packages by automating metadata detection, version bumping, distribution building, and publishing to PyPI.  In this page we walk through two practical examples that illustrate how to use the core API functions in both their simplest form and with a full set of optional parameters.  Each example contains detailed prose explaining why each step is necessary, a parameter table for the function under discussion, and a runnable code snippet that can be copied directly into a Python REPL or script.

Basic Import and Execution
==========================

The most common way to invoke *irelease* is by importing the package and calling :func:`irelease.run` without any arguments.  This pattern is useful for quick, ad‑hoc releases when you are working in the root directory of a repository that follows the standard layout (i.e., it contains either a ``setup.py`` or a ``pyproject.toml``).  By relying on the default parameters, you let *irelease* infer the package name, discover the current version, and perform all subsequent steps automatically.

.. code-block:: python

   # import irelease
   # print(irelease.__version__)

   irelease.run()

Advanced Usage with Parameters
==============================

For more control over the release pipeline, :func:`irelease.run` accepts several optional keyword arguments that allow you to tailor each step of the process.  This is especially useful when working across multiple repositories or when certain stages (such as cleaning the build directory or installing the package locally) need to be skipped.  The following example demonstrates a complete workflow where we specify the repository owner, the package name, disable the clean and install steps, set the Twine version to ``None`` so that the default is used, and increase verbosity for detailed logging.

The rationale behind each parameter is as follows:


Important Notes
---------------

* The module header indicates this is part of the *irelease* project (MIT license).
* ``run()`` can be called with positional arguments for ``repo`` and ``pkg``; keyword arguments are optional.

.. include:: add_bottom.add

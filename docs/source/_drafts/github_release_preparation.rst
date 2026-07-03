github_release_preparation
###########################

Getting the Latest GitHub Release Version
========================================

When preparing a new release of your software it is crucial to know which version number has already been published on GitHub. Relying on manual inspection of the web interface or on ad‑hoc scripts can quickly lead to mistakes, especially in projects with many contributors or frequent releases. The `github_version` helper function abstracts all network communication and semantic‑version logic into a single call, allowing you to retrieve the most recent tag reliably and consistently.

The implementation first determines whether a shallow clone of the repository is required or if it can query the GitHub API directly. In the latter case it performs a GET request against the releases endpoint (`/repos/{owner}/{repo}/releases`), handling pagination automatically so that even repositories with dozens of tags are processed efficiently. Once all tag names have been collected, the function applies semantic‑version ordering to select the highest version. If a leading `v` is present in the tag name it is stripped before returning the result, ensuring that downstream tooling receives a clean version string.

Because many projects use pre‑release or draft tags (for example `v1.2.3-beta`) the function accepts an optional glob pattern (`tag_pattern`) to filter which tags should be considered. By default it looks for tags starting with `v`, but you can override this behavior by passing a custom pattern such as `*beta` or `release-*`. This flexibility makes the helper suitable for both strict semantic‑versioning workflows and more relaxed tagging schemes.

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Parameter
     - Type
     - Description
   * - repo_owner
     - str
     - GitHub username or organization that owns the repository.
   * - repo_name
     - str
     - Name of the target repository.
   * - tag_pattern
     - str, optional
     - Glob pattern used to filter tags; defaults to ``"v*"``.
   * - auth_token
     - str, optional
     - Personal access token for private repositories or higher rate limits; if omitted the function falls back to the `GITHUB_TOKEN` environment variable.

.. code-block:: python

    from irelease import github_version

    # Retrieve latest release from GitHub
    latest = github_version("myorg", "mypackage")
    print(f"Latest released version: {latest}")

Important Notes
---------------

- Ensure network connectivity and that the repository is public or you have a valid token set in `GITHUB_TOKEN`.
- The function expects tag names to follow semantic‑versioning; non‑conforming tags may be ignored.

Backend Notes
-------------

`github_version` is defined in ``irelease.py`` and relies on the `requests` library. It is not exposed by the package's public API, so it must be imported directly from `irelease`. The function does not modify local files; it only reads data from GitHub.

.. include:: add_bottom.add
# irelease

[![Python](https://img.shields.io/pypi/pyversions/irelease.svg)](https://pypi.org/project/irelease/)
[![PyPI](https://img.shields.io/pypi/v/irelease.svg)](https://pypi.org/project/irelease/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-blue.svg)](https://erdogant.github.io/irelease/)
[![Stars](https://img.shields.io/github/stars/erdogant/irelease)](https://github.com/erdogant/irelease)
[![Downloads](https://static.pepy.tech/personalized-badge/irelease?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/irelease)

> iRelease automates and simplifies Python package release workflows. It provides a lightweight command‑line interface that orchestrates GitHub tagging, PyPI publishing, and script generation in one seamless step. With functions such as `github_version` to fetch the latest tag, `get_pypi_credentials` for secure credential handling, and `make_script` to produce reusable bash scripts, users can create reproducible releases without manual scripting. The library’s core entry point forwards CLI arguments to `irelease.main()`, keeping the public API minimal while exposing powerful internals like `run()` for end‑to‑end deployment. iRelease is ideal for developers who want a consistent, automated release pipeline that integrates with GitHub and PyPI, reduces human error, and speeds up continuous delivery cycles.

---

## 📖 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Dependencies](#-dependencies)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)

---

## ✨ Features

- Automates GitHub and PyPI release workflow
- Generates reusable bash release scripts
- Retrieves latest GitHub tag version
- Supports custom package names and options
- Provides verbose logging for debugging

---

## 🚀 Installation

**Stable release (PyPI):**
```bash
pip install irelease
```

**Latest development version:**
```bash
pip install git+https://github.com/erdogant/irelease.git@main
```

**Clone and install locally:**
```bash
git clone https://github.com/erdogant/irelease.git
cd irelease
pip install -e .
```

---

## ⚡ Quick Start

```bash
# Create a release script in the project root
irelease.make_script()
```
```python
# Run the full release process (Git, PyPI, documentation)
import irelease
irelease.run()
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| setuptools | >=42 | Build and package distribution |
| twine | >=3.0 | Upload packages to PyPI |
| gitpython | >=3.1 | Interact with Git repositories |


---

## 📚 Documentation

Full documentation, including API reference and examples, is available at:
**[https://erdogant.github.io/irelease/](https://erdogant.github.io/irelease/)**

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/erdogant/irelease).

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📝 Citation

If you use `irelease` in your research, please cite it as:

```bibtex
@software{irelease,
  author = {erdogant},
  title  = {irelease},
  url    = {https://github.com/erdogant/irelease},
}
```

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/erdogant/irelease/blob/master/LICENSE) file for details.

# irelease - Library that automates releasing your Github python package at Pypi.

[![Python](https://img.shields.io/pypi/pyversions/irelease)](https://img.shields.io/pypi/pyversions/irelease)
[![PyPI Version](https://img.shields.io/pypi/v/irelease)](https://pypi.org/project/irelease/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/irelease/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/irelease.svg)](https://github.com/erdogant/irelease/network)
[![Open Issues](https://img.shields.io/github/issues/erdogant/irelease.svg)](https://github.com/erdogant/irelease/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/irelease/month)](https://pepy.tech/project/irelease/)
[![Downloads](https://pepy.tech/badge/irelease)](https://pepy.tech/project/irelease)
[![DOI](https://zenodo.org/badge/231263493.svg)](https://zenodo.org/badge/latestdoi/231263493)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/irelease/)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://erdogant.github.io/irelease/pages/html/Documentation.html#medium-blog)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/irelease)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/irelease/pages/html/Documentation.html#)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://erdogant.github.io/irelease/pages/html/Documentation.html#colab-notebook)
<!---![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/irelease)-->
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->


Release your library by using the command: ``irelease`` or ``pyrelease``

# 
**Star this repo if you like it! ⭐️**
#

## Introduction
irelease is Python package that will help to release your python package on both github and pypi.
A new release of your package is created by taking the following steps:

1. Extract the version from the __init__.py file
2. Remove old build directories such as dist, build and x.egg-info
3. Git pull (to make sure all is up to date)
4. Get latest release version at github
5. Check if the local (current) version is newer then the latest github release.

        a. Make new wheel, build and install package
        b. Set tag to newest version
        c. Push to git
        d. Upload to pypi (credentials for pypi required)

---------------

### Installation
* Install irelease from PyPI (recommended). irelease is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

### Quick Start
```bash
pip install irelease
```

### Alternatively, install irelease from the GitHub source:
```bash
git clone https://github.com/erdogant/irelease.git
cd irelease
python setup.py install
```


### Run irelease
Go to the directory where the package is you want to release and simply run ``release``:
```bash
$ irelease
```

The following arguments are availble:
```bash
# Github name
irelease -u <githubname>

# Package name your want to release
irelease -p <packagename>

# Removing local builds:
# 1: Yes
# 0: No
irelease -c 1

# Verbosity messages:
# 0: No messages
# 1: Error only
# 2: Warnings and above
# 3: Regular messages and above
# 4: Debug and above
# 5: Trace and above
irelease -v 5

# Twine path for to irelease at pypi. This is automatically determined if standard installation is performed.
irelease -t 'C://Users/erdogant/AppData/Roaming/Python/Python36/Scripts/twine.exe'
```

### Example:
Your package to-be-published must have the correct structure. At least these files and folders are expected:
```bash
    <any_dirname>/
    ├── <package_dir>/
    │   ├── __init__.py
    │   ├── package_name.py
    │   ├── ...
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── ...
```


### Example: releasing bnlearn package.
```bash
    bnlearn/
    ├── bnlearn/
    │   ├── __init__.py
    │   ├── bnlearn.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── setup.py
```
<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig1.png" width="500" />
</p>


#### Go to your destination dir and run release:
```bash
$ irelease
```

**release with your specified arguments**
```bash
# Package can be specified:
$ bnlearn>irelease -p bnlearn

# Username can be specified:
$ bnlearn>irelease -u erdogant

# Cleaning of previous builds in directory can be disabled
$ bnlearn>irelease -c 0
```

<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig2.png" width="600" />
</p>

<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig2b.png" width="600" />
</p>

### Do not forget to enter some release information on github and mark your release number:
<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig3.png" width="600" />
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig4.png" width="600" />
</p>


#### References
* https://github.com/erdogant/irelease

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

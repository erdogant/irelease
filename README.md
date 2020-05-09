# irelease

[![Python](https://img.shields.io/pypi/pyversions/irelease)](https://img.shields.io/pypi/pyversions/irelease)
[![PyPI Version](https://img.shields.io/pypi/v/irelease)](https://pypi.org/project/irelease/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/irelease/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/irelease/month)](https://pepy.tech/project/irelease/month)

**Star it if you like it!**

* irelease is Python package that will help to release your python package on both github and pypi.
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
## Contents
- [Installation](#-installation)
- [Requirements](#-Requirements)
- [Quick Start](#-quick-start)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

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
$ pyrelease
```

The following arguments are availble:
```bash
# Github name
pyrelease -u <githubname>

# Package name your want to release
pyrelease -p <packagename>

# Removing local builds:
# 1: Yes
# 0: No
pyrelease -c 1

# Verbosity messages:
# 0: No messages
# 1: Error only
# 2: Warnings and above
# 3: Regular messages and above
# 4: Debug and above
# 5: Trace and above
pyrelease -v 5

# Twine path for to irelease at pypi. This is automatically determined if standard installation is performed.
pyrelease -t 'C://Users/erdogant/AppData/Roaming/Python/Python36/Scripts/twine.exe'
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
$ pyrelease
```

**release with your specified arguments**
```bash
# Package can be specified:
$ bnlearn>pyrelease -p bnlearn

# Username can be specified:
$ bnlearn>pyrelease -u erdogant

# Cleaning of previous builds in directory can be disabled
$ bnlearn>pyrelease -c 0
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


### Citation
Please cite irelease in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2020irelease,
  title={irelease},
  author={Erdogan Taskesen},
  year={2019},
  howpublished={\url{https://github.com/erdogant/irelease}},
}
```

#### References
* https://github.com/erdogant/irelease

### Maintainer
	Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
	Contributions are welcome.
	This work is created and maintained in my free time. If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated.

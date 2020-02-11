# irelease

[![Python](https://img.shields.io/pypi/pyversions/irelease)](https://img.shields.io/pypi/pyversions/irelease)
[![PyPI Version](https://img.shields.io/pypi/v/irelease)](https://pypi.org/project/irelease/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/irelease/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/irelease/week)](https://pepy.tech/project/irelease/week)
[![Donate Bitcoin](https://img.shields.io/badge/donate-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)

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
pip install -r requirements
pip install irelease
```
### Alternatively, install irelease from the GitHub source:
```bash
git clone https://github.com/erdogant/irelease.git
cd irelease
python setup.py install
```
### Arguments or irelease
Go to the directory where the package is you want to release and run irelease by: 
```bash
$ python irelease.py
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

* To release your package, to most easy way is to generate a release bash file using irlease.
```python
# 1. Go into your package directory
# 2. start ptyhon
# 3. Import irelease, run irelease.get_script()
# 4. A new file (release.sh) is created in your package directory.
# 5. Run it.

# $ python
import irelease
irelease.get_script()
exit()
```
```bash
$ release.sh
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

* Option 1: Create release bash file and run. 
```bash
$ python
>>> import irelease
>>> irelease.get_script()
$ release.sh
```

* Option 2: Run python file. 
```bash
$ bnlearn>python C:\Users\Erdogan\Miniconda3\envs\env_TEST\Lib\site-packages\irelease\irelease.py
```

```bash
# Package can be specified:
$ \bnlearn>python irelease -p bnlearn

# Username can be specified:
$ bnlearn>python irelease.py -u erdogant

# Cleaning of previous builds in directory can be disabled
$ bnlearn>python irelease.py -c 0
```
<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig2.png" width="600" />
</p>

You need to do one final edit on github:
<p align="left">
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig3.png" width="400" />
  <img src="https://github.com/erdogant/irelease/blob/master/docs/figs/fig4.png" width="400" />
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

#### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
#### Contribute
* Contributions are welcome.
#### Licence
See [LICENSE](LICENSE) for details.
#### Donation
* This work is created and maintained in my free time. Contributions of any kind are appreciated. <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Sponsering</a> is also possible.

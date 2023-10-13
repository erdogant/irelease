"""Make new release on github and PyPi."""
# --------------------------------------------------
# Name        : irelease.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/irelease
# Licence     : MIT
# --------------------------------------------------

import sys
import os
import re
# import platform
import argparse
import numpy as np
import urllib.request
import shutil
from packaging import version
import webbrowser
IGNORE_DIRS_IN_PACKAGE = np.array([f for f in os.listdir('.') if os.path.isdir(f) and (f[0]=='.' or f[0]=='_')])
EXCLUDE_DIR = np.unique(np.array(list(IGNORE_DIRS_IN_PACKAGE) + ['build', 'dist', 'doc', 'docs', 'depricated']))


# %% Make executable:
def make_script():
    """Create bash file to release your package.

    Returns
    -------
    release.sh
    release.py

    """
    py_path = os.path.dirname(os.path.abspath(__file__))
    release_path = os.path.join(py_path, 'irelease.py')
    f = open("release.sh", "w")
    f.write('#!/bin/sh')
    f.write('\necho "release your package.."')
    f.write('\npython "' + release_path + '"')
    f.write('\nread -p "Press [Enter] to close"')
    f.close()
    # Copy irelease script
    shutil.copyfile(release_path, os.path.join(os.getcwd(), 'release.py'))
    print('[irelease] release.sh created and .py file copied!')


# %% def main(username, packagename=None, verbose=3):
def run(username, packagename, clean=False, install=False, twine=None, verbose=3):
    """Make new release on git and PyPi.

    Description
    -----------
    A new release is created by taking the underneath steps:
        1. List all files in current directory and exclude all except the directory-of-interest
        2. Extract the version from the __init__.py file
        3. Remove old build directories such as dist, build and x.egg-info
        4. Git pull
        5. Get latest version from github/gitlab
        6. Check if the current version is newer then github latest--version.
            a. Make new wheel, build and install package
            b. Set tag to newest version and push to git
            c. Upload to PyPi (credentials required)

    Parameters
    ----------
    username : str
        Name of the git account.
    packagename : str
        Name of the package.
    clean : bool
        Clean local distribution files for packaging.
    twine : str
        Filepath to the executable of twine.
    verbose : int
        Print message. The default is 3.

    Returns
    -------
    None.

    Examples
    --------
    >>> # Go to the root of the directory package you aim to release and type:
    >>> irelease
    >>> # Description of the input arguments:
    >>> irelease --help

    References
    ----------
    * https:https://github.com/erdogant/irelease
    * https://dzone.com/articles/executable-package-pip-install
    * https://blog.ionelmc.ro/presentations/packaging/#slide:8

    """
    # Set defaults
    username, packagename, clean, install, twine, git, git_pathname, verbose = _set_defaults(username, packagename, clean, install, twine, verbose)
    # Get package name
    packagename = _package_name(packagename, verbose=verbose)
    # Determine github/gitlab

    if packagename is None: raise Exception('[irelease] ERROR: Package directory does not exists.')
    if username is None: raise Exception('[irelease] ERROR: %s name does not exists.' %(git))

    # Get init file from the dir of interest
    initfile = os.path.join(packagename, "__init__.py")

    if verbose>=3:
        if _get_platform()=='windows':
            os.system('cls')
        else:
            os.system('clear')
        print('[irelease] =============================================================================')
        print('[irelease] username  : %s' %username)
        print('[irelease] Package   : %s' %packagename)
        print('[irelease] Git       : %s' %git)
        print('[irelease] Install   : %s' %install)
        print('[irelease] Clean     : %s' %clean)
        print('[irelease] init file : %s' %initfile)
        print('[irelease] =============================================================================')

    if os.path.isfile(initfile):
        # Extract version from __init__.py
        getversion = _getversion(initfile)
        if getversion:
            _try_to_release(username, packagename, getversion, initfile, install, clean, twine, git, git_pathname, verbose)
        else:
            if verbose>=1: print("[irelease] ERROR: Unable to find version string in %s. Make sure that the operators are space seperated eg.: __version__ = '0.1.0'" % (initfile,))
    else:
        if verbose>=2: print('[irelease] Warning: __init__.py File not found: %s' %(initfile))

    if verbose>=3:
        input("[irelease] Press [Enter] to exit.")
        print('[irelease] =============================================================================')


# %% Final message
def _fin_message(username, packagename, current_version, git_version, git, git_pathname, user_input, verbose):
    if user_input=='':
        if verbose>=2:
            print('[irelease] =============================================================================')
            print('[irelease] >  Almost done but one manual action is required:')
            print('[irelease] 1. Go to your %s most recent releases.' %(git))
            print('[irelease] 2. Press botton [Create release from tag]')
            print('[irelease] 3. Set [Release title]: v%s' %(current_version))
            print('[irelease] 4. Make a description in the field: [Create release from Tag]')
            print('[irelease] 5. Press <Publish release> at the bottom of the page.')
            print('[irelease] 6. Fin!')
            print('[irelease] =============================================================================')

        # Open webbroswer and navigate to git to add version
        if verbose>=3: input("[irelease] Press [Enter] to navigate..")
        if git=='github':
            git_release_link = 'https://github.com/' + username + '/' + packagename + '/releases/tag/' + current_version
        elif git=='gitlab':
            git_release_link = 'https://gitlab.com/' + username + git_pathname + packagename + '/-/tags/' + current_version
        webbrowser.open(git_release_link, new=2)
        if verbose>=2:
            print('[irelease] %s' %(git_release_link))
            print('[irelease] =============================================================================')


# %% Get latest github/gitlab version
def github_version(username, packagename, verbose=3):
    """Get latest github version for package.

    Parameters
    ----------
    username : String
        Name of the github account.
    packagename : String
        Name of the package.
    verbose : int, optional
        Print message. The default is 3.

    Returns
    -------
    git_version : String
        x.x.x. : Version number of the latest github package.
        0.0.0  : When repo has no tag/release yet.
        9.9.9  : When repo is private or package/user does not exists.

    """
    # Pull latest from github
    print('[irelease] git pull')
    os.system('git pull')

    # Check whether username/repo exists and not private
    try:
        github_page = None
        github_url = 'https://api.github.com/repos/' + username + '/' + packagename + '/releases'
        github_page = str(urllib.request.urlopen(github_url).read())
        tag_name = re.search('"tag_name"', github_page)
    except:
        if verbose>=1: print('[irelease] ERROR: github %s does not exists or is private.' %(github_url))
        git_version = '9.9.9'
        return git_version

    # Continue and check whether this is the very first tag/release or a multitude are readily there.
    if tag_name is None:
        if verbose>=4: print('[release.debug] github exists but tags and releases are empty [%s]' %(github_url))
        # Tag with 0.0.0 to indicate that this is a very first tag
        git_version = '0.0.0'
    else:
        try:
            # Get the latest release
            github_url = 'https://api.github.com/repos/' + username + '/' + packagename + '/releases/latest'
            github_page = str(urllib.request.urlopen(github_url).read())
            tag_name = re.search('"tag_name"', github_page)
            # Find the next tag by the seperation of the comma. Do +20 or so to make sure a very very long version would also be included.
            # git_version = yaml.load(github_page)['tag_name']
            tag_ver = github_page[tag_name.end() + 1:(tag_name.end() + 20)]
            next_char = re.search(',', tag_ver)
            git_version = tag_ver[:next_char.start()].replace('"', '')
        except:
            if verbose>=1:
                print('[irelease] ERROR: Can not find the latest Github version!')
                print('[irelease] ERROR: Maybe repo Private or does not exists?')
            git_version = '9.9.9'

    if verbose>=4: print('[irelease] Github version: %s' %(git_version))
    if verbose>=4: print('[irelease] Github version requested from: %s' %(github_url))
    return git_version


# %% Helper functions
def _make_build_and_install(packagename, current_version, install):
    # Provide option to continue with the release
    print('[irelease] =============================================================================')
    print("[irelease] Type [Q] to Quit and [Enter] to create the Distribution Archives.")
    print('[irelease] =============================================================================')
    user_input = input("[irelease] > ")

    if user_input=='':
        # Make new build
        print('[irelease] =============================================================================')
        print('[irelease] Making new wheel..')
        print('[irelease] =============================================================================')
        os.system('python setup.py bdist_wheel')
        # Make new build
        print('[irelease] =============================================================================')
        print('[irelease] Making source build..')
        print('[irelease] =============================================================================')
        os.system('python setup.py sdist')
        # Install new wheel
        if install:
            command = 'pip install -U dist/' + packagename + '-' + current_version + '-py3-none-any.whl'
            print('[irelease] =============================================================================')
            print('[irelease] Installing new wheel:\n%s' %(command))
            print('[irelease] =============================================================================')
            os.system(command)
        print('[irelease] =============================================================================')
        print("[irelease] Distribution archives are created on your local machine!")
    return user_input


def _github_set_tag_and_push(current_version, user_input, verbose=3):
    # Push to git and set the Tag.
    # Only continue if the previous state was not to [Q]uit!
    if user_input=='':
        print('[irelease] =============================================================================')
        print("[irelease] Type [Q] to Quit and [Enter] to push to Git and create tag [%s]." %(current_version))
        print('[irelease] =============================================================================')
        user_input = input("[irelease] > ")

        if user_input=='':
            # git commit
            if verbose>=3: print('[irelease] git add->commit->push')
            os.system('git add .')
            os.system('git commit -m ' + current_version)
            # os.system('git commit -m v' + current_version)
            # os.system('git push')
            # Set tag for this version
            if verbose>=3: print('[irelease] Set new version tag: %s' %(current_version))
            # git tag -a 0.1.0 -d "0.1.0"
            # os.system('git tag -a v' + current_version + ' -m "v' + current_version + '"')
            os.system('git tag -a ' + current_version + ' -m "' + current_version + '"')
            os.system('git push origin --tags')

    return user_input


def _make_clean(packagename, verbose=3):
    if verbose>=3: print('[irelease] Removing local build directories..')
    # if os.path.isdir('dist'): shutil.rmtree('dist')
    # if os.path.isdir('build'): shutil.rmtree('build')
    # if os.path.isdir(packagename + '.egg-info'): shutil.rmtree(packagename + '.egg-info')
    directories_to_remove = ['dist',
                            'build',
                            packagename + '.egg-info',
                            os.path.join(packagename, '__pycache__'),
                            os.path.join(packagename, 'tests', '__pycache__'),
                            '.pytest_cache',
                            '.pylint.d']

    for directory in directories_to_remove:
        if os.path.isdir(directory):
            if verbose>=3: print('[irelease] [%s] is removed from packagedir' %(directory))
            shutil.rmtree(directory)


def _get_platform():
    platforms = {
        'linux1': 'linux',
        'linux2': 'linux',
        'darwin': 'osx',
        'win32': 'windows',
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


def _package_name(packagename, verbose=3):
    # Infer name of the package by excluding all known-required-files-and-folders.
    if packagename is None:
        if verbose>=4: print('[irelease] Infer name of the package from the directory..')
        # List all folders in dir
        filesindir = np.array(os.listdir())
        getdirs = filesindir[list(map(lambda x: os.path.isdir(x), filesindir))]
        # Remove all the known not relevant files and dirs
        Iloc = np.isin(np.array(list(map(str.lower, getdirs))), EXCLUDE_DIR)==False  # noqa
        if np.any(Iloc):
            packagename = getdirs[Iloc][0]

    if verbose>=4: print('[irelease] Working on package: [%s]' %(packagename))
    return (packagename)


def _git_host(verbose=3):
    # Extract github/gitlab from config file
    git=None
    f = open('./.git/config')
    gitconfig = f.readlines()
    for line in gitconfig:
        line = line.replace('\t', '')
        if re.search('github.com', line) is not None:
            git = 'github'
        if re.search('gitlab.com', line) is not None:
            git = 'gitlab'
    return git


def _git_username(git, verbose=3):
    # Extract github username from config file
    username=None
    if verbose>=4: print('[release.debug] Extracting github name from .git folder')
    # Open github config file
    f = open('./.git/config')
    gitconfig = f.readlines()
    # Iterate over the lines and search for git@github.com
    for line in gitconfig:
        line = line.replace('\t', '')
        geturl = re.search('@' + git + '.com', line)  # SSH
        if not geturl:
            if git =='gitlab':
                geturl = re.search('https://' + git, line)  # HTTPs
            elif git =='github':
                geturl = re.search('https://' + git + '.com', line)  # HTTPs
        # Extract the username
        if geturl:
            # exract the username
            username_line = line[geturl.end() + 1:(geturl.end() + 20)]
            next_char = re.search('/', username_line)
            username = username_line[:next_char.start()].replace('"', '')

    return username


def _git_pathname(git, username, packagename, verbose=3):
    # Extract github username from config file
    git_pathname = ''
    if verbose>=4: print('[release.debug] Extracting git path from .git folder')
    # Open github config file
    f = open('./.git/config')
    gitconfig = f.readlines()
    # Iterate over the lines and search for git@github.com
    for line in gitconfig:
        line = line.replace('\t', '')
        geturl = re.search('@' + git + '.com', line)  # SSH
        # Extract the pathname
        if geturl:
            repo_line = line[geturl.end():]
            start_pos = re.search(username, repo_line)
            end_pos = re.search(packagename, repo_line)
            if start_pos is not None and end_pos is not None:
                git_pathname = repo_line[start_pos.end():end_pos.start()]

    return git_pathname


# def _package_name(git, verbose=3):
#     # Extract github username from config file
#     package = None
#     if verbose>=4: print('[release.debug] Extracting package name from .git folder')
#     # Open github config file
#     f = open('./.git/config')
#     gitconfig = f.readlines()
#     # Iterate over the lines and search for git@github.com
#     for line in gitconfig:
#         line = line.replace('\t', '')
#         if git=='github':
#             geturl = re.search('@github.com', line)
#         # If git@github.com detected: exract the package
#         if geturl:
#             repo_line = line[geturl.end():]
#             start_pos = re.search('/', repo_line)
#             stop_pos = re.search('.git', repo_line)
#             package = repo_line[start_pos.end():stop_pos.start()].replace('"', '')

#     return package


def _package_name(git, verbose=3):
    # Extract github username from config file
    package = None
    if verbose>=4: print('[release.debug] Extracting package name from .git folder')
    # Open github config file
    f = open('setup.py')
    gitconfig = f.readlines()
    # Iterate over the lines and search for git@github.com
    for line in gitconfig:
        line = line.replace('\t', '')
        geturl = re.search('name=', line)
        # If name= detected: exract the package
        if geturl:
            package = line[geturl.end():]
            package = package.replace('\n', '')
            package = package.replace(',', '')
            package = package.replace("'", '')
            package = package.replace('"', '')

    return package


def _set_defaults(username, packagename, clean, install, twine, verbose):
    # Defaults
    # Default verbosity value is 0
    if verbose is None:
        verbose=3

    if (clean is None) or (clean==1) or (clean is True):
        clean=True
    else:
        clean=False

    if (install==1) or (install is True):
        install=True
    else:
        install=False

    if (twine is None):
        if _get_platform()=='windows':
            twine = os.environ.get('TWIN', None)

    # Get github/gitlab
    git = _git_host(verbose=verbose)

    # Get username
    if (username is None):
        username = _git_username(git, verbose=verbose)

    # Get package name
    if (packagename is None):
        packagename = _package_name(git, verbose=verbose)

    # Pathname
    git_pathname = _git_pathname(git, username, packagename, verbose=verbose)

    return username, packagename, clean, install, twine, git, git_pathname, verbose


def _getversion(initfile):
    # Check version
    return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(initfile, "rt").read(), re.M)


# %% try to Release
def _try_to_release(username, packagename, getversion, initfile, install, clean, twine, git, git_pathname, verbose):
    # Remove build directories
    if verbose>=3 and clean:
        input("[irelease] Press [Enter] to clean previous local builds from the package directory..")
        print('[irelease] =============================================================================')
        _make_clean(packagename, verbose=verbose)
    # Version found, lets move on:
    current_version = getversion.group(1)
    # Get latest version of github release
    if git=='github':
        git_version = github_version(username, packagename, verbose=verbose)
    elif git=='gitlab':
        git_version = '0.0.0'
        if verbose>=3: print("[irelease] Version is not checked on %s." %(git))

    # Print info about the version
    print('[irelease] =============================================================================')
    if git_version=='0.0.0':
        if verbose>=3: print("[irelease] Release package: [%s]" %(packagename))
        VERSION_OK = True
    elif git_version=='9.9.9':
        if verbose>=3: print("[irelease] %s/%s not available at %s." %(username, packagename, git))
        VERSION_OK = False
    elif version.parse(current_version)>version.parse(git_version):
        if verbose>=3: print('[irelease] Current local version from %s: %s and from __init__.py: %s' %(git, git_version, current_version))
        VERSION_OK = True
    else:
        VERSION_OK = False

    if (not VERSION_OK) and (git_version != '9.9.9') and (git_version != '0.0.0'):
        if verbose>=2:
            print('[irelease] WARNING: You may need to increase your version: [%s]' %(initfile))
            print('[irelease] WARNING: Local version : %s' %(current_version))
            print('[irelease] WARNING: %s version: %s' %(git, git_version))

    # Make build and install
    user_input = _make_build_and_install(packagename, current_version, install)
    # Set tag to github and push
    user_input = _github_set_tag_and_push(current_version, user_input, verbose=verbose)
    # Upload to pypi
    user_input = _upload_to_pypi(twine, user_input, verbose=verbose)
    # Fin message and webbrowser
    _fin_message(username, packagename, current_version, git_version, git, git_pathname, user_input, verbose)


# %% Upload to pypi
def _upload_to_pypi(twine, user_input, verbose=3):
    # Push to git and set the Tag.
    # Only continue if the previous state was not to [Q]uit!
    if user_input=='':
        print('[irelease] =============================================================================')
        print("[irelease] Type [Q] to Quit and [Enter] to release on PyPi using Twine.")
        print('[irelease] =============================================================================')
        user_input = input("[irelease] > ")

        if user_input=='':
            bashCommand=''
            if twine is None:
                bashCommand = "twine" + ' upload dist/*'
            elif os.path.isfile(twine):
                bashCommand = twine + ' upload dist/*'

            if verbose>=3: print('[irelease] %s' %(bashCommand))

            try:
                os.system(bashCommand)
            except:
                pass

    # return
    return user_input


# %% Main function
def main():
    """Run the Main function.

    Returns
    -------
    None.

    """
    # main
    parser = argparse.ArgumentParser()
    # parser.add_argument("github", type=str, help="github account name")
    parser.add_argument("-u", "--username", type=str, help="Username on Github/Gitlab..")
    parser.add_argument("-p", "--package", type=str, help="Package name to be released.")
    parser.add_argument("-c", "--clean", type=int, choices=[0, 1], help="Remove local builds: [dist], [build] and [x.egg-info].")
    parser.add_argument("-i", "--install", type=int, choices=[0, 1], help="Install this versions on local machine.")
    parser.add_argument("-t", "--twine", type=str, help="Path to twine in case you have a custom build.")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2, 3, 4, 5], help="Verbosity, higher number tends to more information.")
    args = parser.parse_args()

    # Go to main
    run(args.username, args.package, clean=args.clean, twine=args.twine, verbose=args.verbosity)

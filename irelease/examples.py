# --------------------------------------------------
# Name        : irelease.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/irelease
# Licence     : MIT
# --------------------------------------------------

import irelease
# dir(irelease)
# print(irelease.__version__)

# %%
# irelease.make_script()

# %%
import irelease
irelease.run('erdogant', 'pca', clean=False, install=False, twine=None, verbose=3)



import sys
import os
import pip

def install(package):                                   # Install require file for BMFD
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
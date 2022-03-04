#! python3
# selectiveCopy.py - program walks through a directory tree and searches
# for certain file extensions(.pdf/.jpg) and copied files in a resultFolder

import os
import shutil

path = r'C:\MyPythonScripts\Test'
dir = r'C:\MyPythonScripts\TestCopyTree'

# iterate through a directory tree
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)
        if filename.endswith('.txt'):
            print('Copying %s from %s to %s...' % (filename, foldername, dir))
            filepath = os.path.join(os.path.abspath(foldername), filename)

            if not os.path.exists(dir):
                # Create result folder if it doesn't exist
                os.makedirs(dir)

            if os.path.dirname(filepath) != dir:
                # prevent copying files from result folder
                shutil.copy(filepath, dir)

print('done...')

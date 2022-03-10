#! Python3
# delettingUnaddedFiles - finds files in a directory tree that
# are no longer used and deletes them

import os
import send2trash



path = r'C:\MyPythonScripts\TestCopyTree'


for folderName, subfolders, filenames in os.walk(path):
    for subfolder in subfolders:
        if os.path.getsize(path) > 100000000:
            print(path)
        else:
            continue
    for filename in filenames:
        if os.path.getsize(path) > 100:
            print(filename)
        else:
            print('Test')
            continue



#! Python3
# delettingUnaddedFiles - finds files in a directory tree that
# are no longer used and deletes them

import os
import send2trash


path = r'C:\MyPythonScripts\TestCopyTree'


for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        full_path = os.path.join(folderName, filename)
        if os.path.getsize(full_path) > 10000:
            print('THE ABSOULUTE PATH is: ' + str(full_path))
            #uncomment if you are sure to delete the file
            send2trash.send2trash(full_path)




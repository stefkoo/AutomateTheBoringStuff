#! python3
# backupToZip.py - Copies an enntire folder and its contents into
# a ZIP file whole filename increments

import zipfile
import os

path = r'C:\MyPythonScripts\Test\Test1'


def backupToZip(folder):
    # backup the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder)  # make sure folder is absolute
    # figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number +1

    # Create a zip-File
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Den verzeichnisbaum durchlaufen und alle Dateien
    # in allen Ordnern komprimieren
    for folderName, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (folderName))
        #Fügt den aktuellen order zur Zip-Datei hinzu
        backupZip.write(folderName)
        #Fügt alle Dateien in diesem Ordner zur ZIP-Datei hinzu
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don' backup the backup ZIP files
            backupZip.write(os.path.join(folderName, filename))
        backupZip.close()
        print('Done.')


backupToZip(path)




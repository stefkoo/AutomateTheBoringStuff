import zipfile,os
path = r'C:\MyPythonScripts'
os.chdir(path)
#Erstellt ZipfileObjekt
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


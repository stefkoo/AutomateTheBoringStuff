#! python3
# renamesDates.py - Renames filenames with American MM-DD-YYYY
# date format to European DD-MM-YYYY

import os
import re
import shutil

datePattern = re.compile(r"""^(.*?)    # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

# Iterates through the files in the working directory
path = r'C:\MyPythonScripts\Test\Test1'

for amerFilename in os.listdir(path):
    mo = datePattern.search(amerFilename)

    #skips files without entering a date
    if mo == None:
        continue
    #retrieves the individual parts of the file name
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    #Assemble filenames in European format
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +afterPart
    # get the complete absolute path

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # rename files

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)




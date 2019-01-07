import os
import time
import datetime
import shutil

sourcedir = r'D:\InBox\0.Grouped\test'
imagefiles = os.listdir(sourcedir)

for imagefile in imagefiles:
    fileDate = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(sourcedir,imagefile)))
    datePart = fileDate.date()
    targetdir = datePart.isoformat()

    if not(os.path.isdir(targetdir)):
        os.makedirs(os.path.join(targetdir))

    shutil.move(os.path.join(sourcedir,imagefile),targetdir)



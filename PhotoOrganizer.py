import os
import time
import datetime
import shutil

os.system('cls')

imagefiles = []
Totalfiles = []
NumOfFiles = 0
i=0

sourceDirJpg = 'D:\\InBox\\1.JPG'
sourceDirRAW = 'D:\\InBox\\2.RAW'
targetPath = 'D:\\InBox\\0.Grouped'

print('\n',"Start JPG & MOV file Copy.",'\n')

for path, folders, imagefiles in os.walk(sourceDirJpg):
    Totalfiles += imagefiles
NumOfFiles = len(Totalfiles)

for path, folders, imagefiles in os.walk(sourceDirJpg):
    for imagefile in imagefiles:
        srcPath = os.path.join(path,imagefile)
        fileDate = datetime.datetime.fromtimestamp(os.path.getmtime(srcPath))
        datePart = fileDate.date()
        targetdir = datePart.isoformat()

        dstPath = os.path.join(targetPath,targetdir)

        if not(os.path.isdir(dstPath)):
            os.makedirs(dstPath)
            print("Dest Folder <",dstPath,"> is created.")

        shutil.copy2(srcPath,dstPath)
        i+=1
        print(imagefile," : ",i,"of",NumOfFiles,"JPG files are copied.")
        
i=0
Totalfiles = []

print('\n',"Start RAW file Copy.",'\n')

for path, folders, imagefiles in os.walk(sourceDirRAW):
    Totalfiles += imagefiles
NumOfFiles = len(Totalfiles)

for path, folders, imagefiles in os.walk(sourceDirRAW):
    for imagefile in imagefiles:
        srcPath = os.path.join(path,imagefile)
        fileDate = datetime.datetime.fromtimestamp(os.path.getmtime(srcPath))
        datePart = fileDate.date()
        targetdir = datePart.isoformat()

        dstPath = os.path.join(targetPath,targetdir,"RAW")

        if not(os.path.isdir(dstPath)):
            os.makedirs(dstPath)
            print("Dest RAW Folder <",dstPath,"> is created.")

        shutil.copy2(srcPath,dstPath)
        i+=1
        print(imagefile," : ",i,"of",NumOfFiles,"RAW files are copied.")

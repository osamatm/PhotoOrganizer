import os
import time
import datetime
import shutil

os.system('cls')

starttime = time.time()

imagefiles = []
Totalfiles = []
NumOfFiles = 0
i=0

JpgCounter = 0
MovCounter = 0
RawCounter = 0
OtherCounter = 0

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

        try:
            shutil.copy2(srcPath,dstPath)
        except:
            print("Error Occured while file copy")
        else:
            i+=1
            print(imagefile," : ",i,"of",NumOfFiles,"JPG & MOV files are copied.")
            filename, ext = os.path.splitext(imagefile)
            if ext == ".JPG":
                JpgCounter += 1
            elif ext == ".MOV":
                MovCounter += 1
            else:
                OtherCounter += 1
        
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

        try:
            shutil.copy2(srcPath,dstPath)
        except:
            print("Error Occured while file copy")
        else:
            i+=1
            filename, ext = os.path.splitext(imagefile)
            print(imagefile," : ",i,"of",NumOfFiles,"RAW files are copied.")
            
            if ext == ".RAF":
                RawCounter += 1
            else:
                OtherCounter += 1

endtime = time.time()
elaspetime = endtime-starttime

minutes, seconds = divmod(elaspetime, 60) 
minutes = round(minutes)
seconds = round(seconds)

print('\n')
print("********************************************")
print("*               Copy Report                *")
print("********************************************")
print("*       ",format(JpgCounter,'05'),"JPG files are copied        *")
print("*       ",format(MovCounter,'05'),"MOV files are copied        *")
print("*       ",format(RawCounter,'05'),"RAW files are copied        *")
print("*       ",format(OtherCounter,'05'),"Other files are copied      *")
print("*       ",format(minutes,'02'),"m",format(seconds,'02'),"s elapsed                 *")
print("********************************************")
print('\n')

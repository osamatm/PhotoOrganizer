import os
import shutil
import glob
import copy
import time

starttime = time.time()

targetDir = 'D:\\Inbox\\0.Grouped'

ResultJpgList = []
ResultRawList = []
JpgList = []
RawList = []
RemainedJpgList = []
RemainedRawList = []
MatchedFileCount = 0
NotMatchedFileCount = 0

folderlist = os.listdir(targetDir)

for folder in folderlist:
    JpgList = glob.glob(targetDir+os.sep+folder+os.sep+'*.JPG', recursive=False)
    RawList = glob.glob(targetDir+os.sep+folder+os.sep+'RAW'+os.sep+'*.RAF', recursive=False)

    ResultJpgList = copy.deepcopy(JpgList)
    #ResultRawList = copy.deepcopy(RawList)

    for jpgfile in JpgList:
        jpath, jname =os.path.split(jpgfile)
        jpgname, jpgext = os.path.splitext(jname)
        for rawfile in RawList:
            rpath, rname =os.path.split(rawfile)
            rawname, rawext = os.path.splitext(rname)    
            if jpgname == rawname:
                MatchedFileCount += 1
                ResultJpgList.remove(jpgfile)
                RawList.remove(rawfile)
                break
            else:
                if rawfile == RawList[-1]:
                    NotMatchedFileCount += 1
    
    RemainedJpgList += ResultJpgList
    RemainedRawList += RawList

endtime = time.time()
executiontime = (endtime-starttime) * 1000
sec, msec = divmod(executiontime, 1000)
sec = round(sec)
msec = round(msec)

print ('\n')
print ("********************************************")
print ("*    RAW & JPG Files Match Check Report    *")
print ("*   ",format(MatchedFileCount,'05'),'JPG & RAW files are matched',"    *")
print ("*   ",format(NotMatchedFileCount,'05'),'JPG files are not matched',"      *")
print ("********************************************")
print ("JPG List:", RemainedJpgList)
print ("RAW List:", RemainedRawList)
print ("********************************************")

print ("Execution Time :",sec,'sec',msec,'msec')

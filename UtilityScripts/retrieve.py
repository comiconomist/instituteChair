# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:45:36 2016

@author: Comiconomist

Script to retrieve any files in Fallout 4's folders that are more recent than
current copies in mod working folder

Only copies files with .ba2 and .esp file types for now.

"""

import os
import datetime
import shutil

acceptableFileTypes = ['.ba2', '.esp']

# Current direcoty:

# Go to Fallout 4 folder of mod working directory:
print(os.getcwd())
os.chdir('..')
projDir = os.getcwd()
projName = projDir.split("\\")[-1]

os.chdir('./Fallout 4')
modWorkfo4Dir = os.getcwd()
#modWorkfo4Dir = 'C:\\Games\\fo4_modding\\Projects\\instituteChair\\Fallout 4'

# True fallout 4 directory:
fo4Dir = 'C:\\Steam\\steamapps\\common\\Fallout 4'

# Get list of files in working directory with relative paths
fileRelPathList = []
for dir_, _, files in os.walk(modWorkfo4Dir):
    for fileName in files:
        relDir = os.path.relpath(dir_, modWorkfo4Dir)
        relFile = os.path.join(relDir, fileName)
        if relFile[-4:] in acceptableFileTypes:
            fileRelPathList.append(relFile)

# Add to the list possible .esp and .ba2 files:
fileRelPathList.append('Data\\' + projName + '.ba2')
fileRelPathList.append('Data\\' + projName + '.esp')

# Loop over files in my mod working directory: if a more recent copy exists in
# the fallout 4 root directory I have probably used the creation kit, so copy
# the more recent one
for myFile in fileRelPathList:
    if os.path.isfile(fo4Dir + '\\' + myFile):
        if os.path.isfile(modWorkfo4Dir + '\\' + myFile):
            # Fallout 4 root directory time:
            fo4Time = os.path.getmtime(fo4Dir + '\\' + myFile)
            fo4TimeStr = datetime.datetime.fromtimestamp(fo4Time).strftime('%Y-%m-%d %H:%M:%S')
            # New mod time:
            modTime = os.path.getmtime(modWorkfo4Dir + '\\' + myFile)
            modTimeStr = datetime.datetime.fromtimestamp(modTime).strftime('%Y-%m-%d %H:%M:%S')
            print(myFile + ' fo4Time: ' + fo4TimeStr + ' modTime: ' + modTimeStr)
            if fo4Time > modTime :
                print('Copying ' + myFile + ' from fo4 to mod working directory')
                shutil.copyfile(fo4Dir + '\\' + myFile, modWorkfo4Dir + '\\' + myFile)
        else:
            print(myFile + 'only exists in fo4 directory')
            print('Copying ' + myFile + ' from fo4 to mod working directory')
            shutil.copyfile(fo4Dir + '\\' + myFile, modWorkfo4Dir + '\\' + myFile)
            
        
print('Copying complete')
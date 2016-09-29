# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:45:36 2016

@author: Comiconomist

Script that deploys files from mod working folder to fo4 folder.

"""

import os
import datetime
import shutil

# Go to Fallout 4 folder of mod working directory:
print(os.getcwd())
os.chdir('../Fallout 4')
modWorkfo4Dir = os.getcwd();

# True fallout 4 directory:
fo4Dir = 'C:\\Steam\\steamapps\\common\\Fallout 4'

# Get list of files in working directory with relative paths
fileRelPathList = []
for dir_, _, files in os.walk(modWorkfo4Dir):
    for fileName in files:
        relDir = os.path.relpath(dir_, modWorkfo4Dir)
        relFile = os.path.join(relDir, fileName)
        fileRelPathList.append(relFile)

# Loop over files in my mod working directory and copy them to fo4 directory
for myFile in fileRelPathList:
    if os.path.isfile(fo4Dir + '\\' + myFile):
        # Fallout 4 root directory time:
        fo4Time = os.path.getmtime(fo4Dir + '\\' + myFile)
        fo4TimeStr = datetime.datetime.fromtimestamp(fo4Time).strftime('%Y-%m-%d %H:%M:%S')
        # New mod time:
        modTime = os.path.getmtime(modWorkfo4Dir + '\\' + myFile)
        modTimeStr = datetime.datetime.fromtimestamp(modTime).strftime('%Y-%m-%d %H:%M:%S')
        print(myFile + ' fo4Time: ' + fo4TimeStr + ' modTime: ' + modTimeStr)
        print('Copying ' + myFile + ' from mod working directory to fo4')
        shutil.copyfile(modWorkfo4Dir + '\\' + myFile, fo4Dir + '\\' + myFile)
        
print('Copying complete')
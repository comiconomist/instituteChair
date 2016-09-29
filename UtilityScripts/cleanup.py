# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:45:36 2016

@author: Comiconomist

Script to remove working mod files from fallout 4 data directory

"""
import os

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

# Loop over files in my mod working directory: delete file in fallout 4 directory
for myFile in fileRelPathList:
    if os.path.isfile(fo4Dir + '\\' + myFile):
        os.remove(fo4Dir + '\\' + myFile) 
        
print('Deletions complete')
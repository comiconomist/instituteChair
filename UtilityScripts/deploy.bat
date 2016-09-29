@echo off
:Ask
echo This will copy ALL files from the current mod working directory to the fallout 4 directory.
echo It will overwrite any .esp and .ba2 that haven't been retrieves since they were updated.
timeout 5 >null
echo Are you sure?(Y/N)
set INPUT=
set /P INPUT=Type input: %=%
If /I "%INPUT%"=="y" goto yes 
If /I "%INPUT%"=="n" goto no
:yes
python deploy.py
:no
PAUSE
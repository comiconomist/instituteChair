@echo off
:Ask
echo This will delete ALL files from the fallout 4 directory that are also in the current mod working directory.
timeout 2 >null
PAUSE
echo This includes .esp and .ba2 that haven't been retrieved since they were updated.
timeout 2 >null
PAUSE
echo Did you remember to retrieve .esp and .ba2 files?.
timeout 2 >null
PAUSE
echo Really?
timeout 2 >null
PAUSE
echo Are you sure?(Y/N)
set INPUT=
set /P INPUT=Type input: %=%
If /I "%INPUT%"=="y" goto yes 
If /I "%INPUT%"=="n" goto no
:yes
python deploy.py
:no
PAUSE
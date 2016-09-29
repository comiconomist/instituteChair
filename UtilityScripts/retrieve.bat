@echo off
:Ask
echo This will overwrite all .esp and .ba2 files in your mod working folder with more recent ones in your fallout 4 folder.
timeout 5 >null
echo Are you sure?(Y/N)
set INPUT=
set /P INPUT=Type input: %=%
If /I "%INPUT%"=="y" goto yes 
If /I "%INPUT%"=="n" goto no
:yes
python retrieve.py
:no
PAUSE
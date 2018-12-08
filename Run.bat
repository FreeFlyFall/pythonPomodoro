@echo off
rem Batch file for running python pomodoro timer in the current directory
rem Place in shell:startup with the program to start it on startup for windows
set file=pythonPomodoroGUI.py
echo Opening %file%
python %file%
exit()
@echo off
rem Batch file for running python pomodoro timer
rem Place in shell:startup to start the program on startup on windows
set file=pythonPomodoroGUI.py
echo Opening %file%
python %file%
exit()
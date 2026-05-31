@echo off
cd /d "%~dp0"
set PY_PATH=C:\Users\DESKTOP\AppData\Local\Programs\Python\Python312\python.exe
powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c cd /d "%~dp0" && "%PY_PATH%" serve_mobile.py'"

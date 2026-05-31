@echo off
cd /d "%~dp0"
echo Stopping background mobile server...
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*serve_mobile.py*' -and $_.Name -match 'python.exe|pythonw.exe' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host 'Stopped process' $_.ProcessId }"
echo Done.
pause

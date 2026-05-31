@echo off
cd /d "%~dp0"
echo Starting mobile server in the background...
set PY_PATH=C:\Users\DESKTOP\AppData\Local\Programs\Python\Python312\python.exe
set LOCAL_IP=127.0.0.1
for /f "delims=" %%I in ('"%PY_PATH%" -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect((\"8.8.8.8\", 80)); print(s.getsockname()[0]); s.close()"') do set LOCAL_IP=%%I
powershell -NoProfile -WindowStyle Hidden -Command "Start-Process -FilePath '%PY_PATH%' -ArgumentList 'serve_mobile.py' -WorkingDirectory '%CD%'"
if errorlevel 1 (
    echo 서버 시작에 실패했습니다.
    pause
) else (
    echo 서버가 백그라운드에서 실행되었습니다.
    echo 모바일에서 접속하려면 http://%LOCAL_IP%:8000/index.html 을 사용하거나 qr_mobile_network.png를 스캔하세요.
    echo 로그는 mobile_server.log 파일에서 확인할 수 있습니다.
)

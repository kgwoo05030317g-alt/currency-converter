@echo off
cd /d "%~dp0"
echo Starting local network server for mobile access...
"C:\Users\DESKTOP\AppData\Local\Programs\Python\Python312\python.exe" serve_mobile.py
if errorlevel 1 (
    echo.
    echo 서버 시작에 실패했습니다. 아래 확인 사항을 다시 확인하세요.
    echo - 같은 Wi-Fi에 연결되어 있는지
    echo - 포트 8000이 다른 프로그램에서 사용 중인지
    echo - 필요하면 run_mobile_server_admin.bat을 관리자 권한으로 실행
    pause
)

# 환율 변환기 웹사이트

Python Flask 앱입니다. 대한민국 1000원이 입력한 나라 화폐로 얼마인지 Yahoo Finance에서 환율 정보를 가져와 계산합니다.

## 설치

1. 프로젝트 폴더로 이동
```
cd C:\Users\DESKTOP\currency_converter
```
2. 가상환경 생성 및 활성화
```
python -m venv venv
.\venv\Scripts\activate
```
3. 패키지 설치
```
pip install -r requirements.txt
```

## 실행

```
python app.py
```

웹 브라우저에서 `http://127.0.0.1:5000`에 접속합니다.

## 브라우저 전용 버전

`index.html` 파일을 브라우저로 바로 열면 Python이 없어도 동작합니다.

- `currency_converter/index.html`을 더블 클릭하여 실행하면 바로 웹 앱이 열립니다.
- `open_site.bat`을 실행하면 기본 브라우저에서 `index.html`을 엽니다.
- 또는 정적 웹 서버(예: GitHub Pages, Vercel, Netlify)로 배포

## 공개 호스팅 (아무 컴퓨터에서 접속)

이 사이트를 인터넷에 공개하면 어떤 컴퓨터에서도 접속할 수 있습니다. 정적 HTML 파일이므로 Python 없이도 가능합니다.

추천 방법:

- GitHub Pages: `index.html` 파일과 필요한 리소스를 GitHub 저장소에 올리고 Pages를 활성화
- Netlify / Vercel: 폴더를 드래그 앤 드롭하여 배포

배포 후에는 `https://<아이디>.github.io/<저장소명>/` 같은 주소로 접속할 수 있습니다.

자세한 배포 방법은 `PUBLIC_HOSTING.md`를 참고하세요.

## 모바일 접근

같은 Wi-Fi에 연결된 휴대폰에서 아래 URL을 열면 모바일에서 바로 접속할 수 있습니다.

- `http://192.168.219.104:8000/index.html`

PC에서 서버를 시작하려면 `run_mobile_server.bat`을 실행하세요.

콘솔 창을 닫아도 계속 실행하려면 `run_mobile_server_hidden.bat`을 사용하세요.

- `run_mobile_server.bat`: 현재 터미널 창에서 서버를 실행합니다.
- `run_mobile_server_hidden.bat`: 터미널 없이 백그라운드에서 서버를 실행합니다.
- `stop_mobile_server.bat`: 백그라운드에서 실행 중인 모바일 서버를 종료합니다.

`run_mobile_server.bat` 또는 `run_mobile_server_hidden.bat` 실행 시 실제 PC 네트워크 IP를 자동으로 찾아 접속 URL을 표시합니다.

> 모바일에서 열려면 PC에서 서버가 켜져 있어야 합니다. `run_mobile_server_hidden.bat`을 실행하면 터미널 창을 닫아도 서버가 계속 동작합니다.

만약 모바일에서 접속이 되지 않으면, 다음을 확인하세요:

- PC와 모바일이 같은 Wi-Fi 네트워크에 연결되어 있는지 확인
- Windows 방화벽이 포트 `8000`을 차단하지 않는지 확인
- 필요하면 `run_mobile_server_admin.bat`을 관리자 권한으로 실행하여 서버를 시작
- 백그라운드 서버 로그는 `mobile_server.log`에서 확인하세요

### QR 코드로 접근하기

아래 QR 코드를 사용하면 모바일에서 더 쉽게 접속할 수 있습니다.

- `qr_mobile_network.png`: 같은 Wi-Fi에서 `http://192.168.219.104:8000/index.html`로 모바일 접속할 때 사용

![Mobile network QR](qr_mobile_network.png)

> 모바일에서는 `qr_mobile_network.png`를 사용하고, PC에서는 `open_site.bat` 또는 `index.html`을 여는 것이 가장 안전합니다.

## 사용 방법

- 나라 이름 입력: 예: `미국`, `일본`, `유럽`, `중국`, `영국`, `호주` 등
- 1000원을 해당 나라 화폐로 환산한 값을 화면에서 확인합니다.

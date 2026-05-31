# 공개 호스팅 안내

이 프로젝트의 `index.html`은 정적 웹 앱입니다. 따라서 인터넷에 올리면 어떤 컴퓨터와 스마트폰에서도 접속할 수 있습니다.

## 1. GitHub Pages로 배포하기

1. GitHub 계정을 만듭니다.
2. 새 저장소를 생성합니다. 예: `currency-converter`.
3. `index.html`과 `README.md`, 필요한 파일을 저장소에 업로드합니다.
4. GitHub 저장소의 Settings > Pages 또는 GitHub Pages 섹션에서 배포 브랜치(`main` 또는 `gh-pages`)를 선택합니다.
5. 배포가 완료되면 공개 주소가 표시됩니다.

예: `https://<GitHub사용자명>.github.io/currency-converter/`

## 2. Netlify로 배포하기

1. Netlify에 로그인하거나 회원가입합니다.
2. "Sites"에서 "New site from Git"을 선택합니다.
3. GitHub 저장소를 연결하고 `currency-converter` 저장소를 선택합니다.
4. 빌드 명령은 필요 없으며, 배포 디렉터리는 `.` 로 설정합니다.
5. 배포 후 제공되는 URL을 공유하면 됩니다.

## 3. Vercel로 배포하기

1. Vercel에 로그인하거나 회원가입합니다.
2. "New Project"를 선택하고 GitHub 저장소를 연결합니다.
3. 정적 사이트로 설정하면 별도 빌드 없이 배포됩니다.
4. 배포된 URL을 사용하여 누구나 접속할 수 있습니다.

## 4. 바로 쓰는 방법

- `index.html`만 호스팅하면 됩니다.
- `webapp/` 폴더가 있다면 동일하게 함께 업로드하세요.
- 외부에서 접근할 수 있는 공개 URL이 생기면, 그 URL을 모든 컴퓨터에서 열 수 있습니다.

## 5. 참고

- `file:///` 주소는 해당 PC에서만 열립니다.
- `http://192.168.x.x:8000` 주소는 같은 로컬 네트워크에 연결된 장치에서만 열립니다.
- 공개 호스팅을 쓰면 인터넷에 연결된 어느 곳에서도 접속할 수 있습니다.

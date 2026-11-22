# 개인용 Rainbow Lab

휴대폰에서 HTML 파일을 직접 여는 대신 **GitHub Pages 웹주소**로 접속해야 합니다.

## 설치
1. GitHub에서 새 저장소 `rainbow-lab`을 만들고 **Public**으로 설정합니다. (GitHub 무료 플랜의 Pages 사용을 위한 가장 간단한 설정입니다.)
2. 이 ZIP의 **내용물 전체**를 저장소 최상위 경로에 업로드합니다. `.github/workflows/update.yml` 파일도 반드시 포함해야 합니다. ZIP 자체를 한 파일로 올리면 안 됩니다.
3. 저장소 **Settings → Actions → General → Workflow permissions**에서 **Read and write permissions**를 선택합니다.
4. **Actions → Update stock data → Run workflow**를 눌러 최초 데이터를 생성합니다. 작업 완료 후 `data/SOXX.json`이 생겼는지 확인합니다.
5. **Settings → Pages → Build and deployment → Deploy from a branch**, `main` / `(root)`를 선택하고 저장합니다.
6. 잠시 뒤 `https://사용자명.github.io/rainbow-lab/`로 접속합니다. 이 주소를 휴대폰 홈 화면에 추가할 수 있습니다.

## 자동 갱신
GitHub Actions가 평일 UTC 23:35(한국시간 다음 날 오전 8:35)에 시세 데이터를 갱신하도록 예약되어 있습니다. 예약 실행은 지연되거나 누락될 수 있고, Yahoo Finance 접근 제한으로 일부 종목이 갱신되지 않을 수 있습니다. 화면에 마지막 데이터 기준일을 확인하세요. 종목 추가는 `update_data.py`의 `TICKERS`에 추가하고 Actions를 다시 실행하면 됩니다. 차트의 가격은 배당/분할 조정 주간 종가이며 실시간 시세가 아닙니다.

## 참고
GitHub Public 저장소의 소스코드와 데이터는 공개됩니다. 사이트에 개인 계정정보나 API 키를 넣지 마세요. 차트는 통계적 로그 회귀 채널이며 투자 가치평가를 보장하지 않습니다.

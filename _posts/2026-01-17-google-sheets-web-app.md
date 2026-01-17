안녕하세요, JNCD입니다.

우리는 언제나 '최소한의 노력으로 최대한의 성과'를 내는 것을 목표로 합니다. 야근은 미래의 나에게 빚을 지는 행위니까요. 오늘은 단순히 데이터를 쌓아두는 스프레드시트를 넘어, 구글 시트를 '나만의 디지털 공작소'로 개조하여 퇴근 시간을 앞당기는 방법에 대해 이야기해 보려 합니다.

이 글은 구글 시트를 엔진으로 삼아 웹 앱(Web App)을 배포하고, AI를 활용해 코딩 한 줄 없이도 커스텀 서비스를 구축하는 기술적인 로드맵을 담고 있습니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_1.png"
alt="그림1: 구글 시트 웹앱 배포 및 AI 활용 가이드 표지"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 1. 구글 시트로 여는 나만의 디지털 공작소*

### 1. 웹 앱(Web App): 시트 밖으로 나온 프로그램

구글 시트는 단순한 문서 도구가 아닙니다. 여러분의 앱이 살아 숨 쉬는 '엔진룸'이 될 수 있습니다. 웹 앱의 개념은 구글 앱스 스크립트(GAS)로 작성한 코드를 독립적인 웹사이트처럼 배포하는 기술입니다.

가장 큰 장점은 **서버리스(Serverless)**라는 점입니다. 별도의 서버를 구매하거나 구축할 필요 없이, 모든 코드는 구글 서버에서 돌아갑니다. 고유한 URL이 생성되므로 링크만 있으면 누구나 내가 만든 도구에 접속할 수 있습니다. 인프라 관리는 구글에게 맡기고 우리는 서비스만 생각합시다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_2.png"
alt="그림2: 웹 앱의 개념과 서버리스 특징 설명"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 2. 웹 앱의 개념: 서버리스와 접근성*

### 2. API: 데이터가 오고 가는 파이프라인

웹 앱은 데이터가 오고 가는 파이프라인 역할을 합니다. 이때 핵심이 되는 두 가지 함수가 있습니다.

* **doGet(e):** 누군가 내 웹 앱 주소를 '방문'하거나 데이터를 '조회'할 때 실행됩니다 (GET 요청).
* **doPost(e):** 누군가 내 웹 앱에 데이터를 '제출'하거나 '저장'할 때 실행됩니다 (POST 요청).

앱스 스크립트의 `ContentService`와 `HtmlService`를 활용하면 단순 텍스트나 JSON 데이터뿐만 아니라 완전한 HTML 페이지까지 반환할 수 있습니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_3.png"
alt="그림3: doGet과 doPost를 이용한 데이터 파이프라인 구조"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 3. 데이터 파이프라인: doGet과 doPost*

### 3. API로 활용 가능한 웹앱의 장점 (Backend Power)

웹 앱을 백엔드로 활용하면 엄청난 효율을 얻을 수 있습니다. 이것이 바로 우리가 '게으른 개발'을 할 수 있는 이유입니다.

* **무료 데이터베이스(Free DB):** 복잡한 SQL을 몰라도 됩니다. 익숙한 엑셀(시트) 인터페이스로 데이터를 관리하고 저장하세요.
* **Headless Mode:** 화면(UI) 없이 순수한 데이터(JSON/Text)만 주고받을 수 있어 다른 웹사이트나 모바일 앱의 백엔드로도 쓸 수 있습니다.
* **연결성(Connectivity):** 외부 서비스의 데이터를 시트로 자동 수집하거나, 반대로 시트의 데이터를 외부로 실시간 전송할 수 있습니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_4.png"
alt="그림4: 무료 DB 및 연결성 등 웹앱 백엔드의 장점"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 4. 백엔드로서의 강점: 무료 DB와 연결성*

### 4. HTML 파일을 활용한 무한한 디자인 자유도

구글 설문지(Forms)의 정해진 틀이 답답하셨나요? `HtmlService`를 사용하면 표준 HTML, CSS, JavaScript를 모두 사용할 수 있어 디자인 자유도가 무한합니다.

버튼의 모양, 색상, 배치를 픽셀 단위로 제어하는 것은 물론, 애니메이션이나 팝업 같은 동적인 상호작용이 가능한 '진짜' 웹사이트를 만들 수 있습니다. 나만의 얼굴을 가진 커스텀 UI를 구현해 보세요.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_5.png"
alt="그림5: HTML 파일을 활용한 커스텀 디자인과 코드 예시"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 5. HTML 서비스를 통한 디자인 자유도*

### 5. AI와 함께하는 정교화 & 디자인 (The Magic Tool)

"저는 디자인 감각도 없고 HTML도 모르는데요?"라고 걱정하실 필요 없습니다. AI가 그 장벽을 허물어 주니까요.

**'프롬프트 투 코드(Prompt to Code)'** 시대로, "파스텔 톤의 둥근 버튼이 있는 로그인 페이지를 만들어줘"라고 AI에게 요청하면 됩니다. AI가 생성한 코드를 앱스 스크립트에 붙여넣기만 하세요. 우리는 코드를 '짜는' 게 아니라 '조립'하는 겁니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_6.png"
alt="그림6: AI를 활용한 코딩 및 디자인 정교화"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 6. AI를 활용한 코드 생성과 디자인*

AI를 활용한 개발 워크플로우는 다음과 같이 단순화됩니다.

1. **명확한 지시:** 원하는 기능과 디자인 스타일을 구체적으로 설명합니다. (예: '반응형 웹으로 만들어줘')
2. **코드 생성 및 수정:** AI가 짜준 백엔드(.gs)와 프론트엔드(.html) 코드를 프로젝트에 적용합니다.
3. **디버깅의 혁신:** 오류가 나면 에러 메시지를 그대로 AI에게 던지세요. 'AI 디버거'가 즉시 수정 코드를 제안합니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_7.png"
alt="그림7: AI를 활용한 3단계 개발 워크플로우"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 7. AI 개발 워크플로우: 지시, 생성, 디버깅*

### 6. 왜 구글 설문지(Forms)로는 부족할까요?

구글 설문지는 간편하지만 한계가 명확합니다. 반면 웹 앱은 다릅니다.

* **디자인:** 폰트나 배경 변경의 제약이 없습니다. 브랜드 아이덴티티를 온전히 반영할 수 있습니다.
* **로직:** 복잡한 데이터 검증 로직을 구현할 수 있습니다.
* **보안 및 데이터:** 로그인 권한을 관리하고, 데이터를 가공해서 저장하는 것이 가능합니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_8.png"
alt="그림8: 구글 설문지와 웹 앱의 차이점 비교"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 8. 구글 설문지 vs 커스텀 웹 앱 비교*

### 활용 사례 1: 스마트한 승인 및 신청 시스템

단순한 설문지를 넘어, 사내 도서 구매나 휴가 신청 시스템을 구축한다고 상상해 봅시다.

1. **자동 완성:** 접속한 사용자의 이름과 부서를 자동으로 불러옵니다 (`Session.getActiveUser()`). 사용자가 굳이 입력하게 만들지 마세요.
2. **데이터 검증:** 입력된 정보가 유효한지, 예산 범위 내인지 제출 버튼을 누르기 *전*에 확인합니다.
3. **히든 데이터:** 사용자는 볼 필요 없지만 관리자에게 필요한 승인 코드나 타임스탬프를 안전하게 함께 전송합니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_9.png"
alt="그림9: 스마트한 승인 및 신청 시스템 활용 사례"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 9. 활용 사례: 스마트 승인 시스템*

### 활용 사례 2: 이미지와 함께하는 재고 목록

텍스트만 있는 목록 대신 시각적인 재고 관리 시스템도 가능합니다.

* **시각적 데이터:** `IMAGE` 함수나 URL로 저장된 제품 사진을 갤러리 형태로 보여줍니다.
* **동적 재고 확인:** 구글 시트의 재고 수량과 실시간으로 연동하여, 품절된 상품은 아예 선택할 수 없게 만듭니다.
* **바코드/QR 생성:** 외부 API와 연동해 제품별 코드를 실시간으로 화면에 띄웁니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_10.png"
alt="그림10: 이미지와 동적 기능을 활용한 재고 목록 사례"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 10. 활용 사례: 시각적 재고 관리 목록*

### 배포 방식의 이해: Bound vs Standalone

스크립트를 배포하는 방식은 크게 두 가지가 있습니다. 상황에 맞게 선택하세요.

* **Container-bound Script (종속형):** 특정 스프레드시트 파일에 묶여 있습니다. 해당 시트의 데이터를 다루기에 가장 빠르고 간편해서 초보자에게 추천합니다.
* **Standalone Script (독립형):** 구글 드라이브에 별도 파일로 존재합니다. 여러 시트를 동시에 관리하거나 라이브러리로 쓸 때 적합합니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_11.png"
alt="그림11: 종속형 스크립트와 독립형 스크립트의 배포 방식 비교"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 11. 배포 방식: 종속형 vs 독립형*

### 배포 설정 (Deployment): 문을 여는 방법

배포할 때 권한 설정은 보안과 직결되므로 중요합니다.

* **실행 권한 (Execute as):**
* **나(Me):** 사용자가 누구든 내 권한으로 실행됩니다. (데이터 보안 유지에 유리)
* **사용자(User):** 접속한 사람의 권한으로 실행됩니다. (개인별 데이터 추적에 유리)


* **액세스 권한 (Who has access):**
* **나만:** 테스트 용도입니다.
* **Google 계정이 있는 모든 사용자:** 사내 도구로 적합합니다.
* **모든 사용자(Anyone):** 로그인 없이 누구나 접속 가능한 퍼블릭 웹 앱입니다.



<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_12.png"
alt="그림12: 실행 권한 및 액세스 권한 설정 화면"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 12. 배포 설정: 실행 및 액세스 권한*

### 확장 기능: 외부 세상과의 연결 (UrlFetchApp)

`UrlFetchApp` 클래스를 사용하면 구글 시트가 외부 세상과 대화할 수 있습니다.

* **Slack 알림:** 신청서가 제출되면 즉시 슬랙 채널로 알림을 보냅니다.
* **AI 요약:** 시트에 쌓인 고객 피드백을 OpenAI API로 보내 감정 분석을 시키고 결과를 저장합니다.
* **데이터 수집:** 외부 서비스와 통신하여 필요한 데이터를 가져오거나 보냅니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_13.png"
alt="그림13: UrlFetchApp을 이용한 외부 서비스 연결 및 확장"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 13. 확장 기능: UrlFetchApp을 통한 외부 연결*

### 나만의 웹 서비스 구축 로드맵

이제 여러분은 전문가입니다. 다음 5단계로 나만의 서비스를 시작해 보세요.

1. **기획:** 구글 시트에 데이터 구조를 설계합니다.
2. **로직:** 앱스 스크립트(`doGet`, `doPost`)로 데이터 처리 규칙을 짭니다.
3. **디자인:** AI를 활용해 HTML/CSS 프론트엔드를 제작합니다.
4. **배포:** 권한 설정 후 웹 앱 URL을 생성합니다.
5. **확장:** 외부 API를 연결해 기능을 고도화합니다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_14.png"
alt="그림14: 웹 서비스 구축을 위한 5단계 로드맵"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 14. 구축 로드맵: 기획부터 확장까지*

복잡한 코딩 공부보다 중요한 것은 '무엇을 만들까' 하는 상상력입니다. 구글 시트와 AI라는 강력한 도구가 준비되어 있습니다. 지금 바로 `script.google.com`에 접속해서 당신만의 첫 번째 '디지털 점토'를 빚어보세요.

남는 시간에는 더 중요한 일(또는 딴짓)을 합시다.

<img src="/assets/images/Sheets_to_Custom_Web_Apps_page_15.png"
alt="그림15: 시작을 독려하는 메시지와 접속 주소"
style="max-width:720px;width:100%;display:block;margin:24px auto;" />
*그림 15. 마무리: 지금 바로 시작하세요*
# SNS


## 목차
<br>

1. [Summary](#-summary)
2. [사용 기술](#-사용-기술)
3. [배포](#-배포)
4. [ERD](#-erd)
5. [Task 관리](#-task-관리)
6. [API 명세서](#-api-명세서)
7. [브랜치 전략](#-브랜치-전략)
8. [컨벤션](#-코드-컨벤션)
9. [API 호출 테스트](#-api-호출-테스트)


<br>

## ✅ Summary
<br>

- 사용자가 게시물로써 소통하는 Social network service 입니다.

<br>

- AWS RDS, EC2, Docker-compose, Gunicorn, NGINX를 사용하여 배포했습니다.

<br>

- 인증은 JWT 토큰으로 이루어집니다.
- 회원가입, 로그인 기능을 제공합니다.
- 카카오 서비스를 이용한 회원가입, 로그인 기능을 제공합니다.

<br>

- 인증된 사용자는 자신의 계정의 정보를 수정, 삭제 할 수 있습니다.
- 삭제된 계정 복구시에는 인증이 필요하지 않습니다.

<br>

- 인증된 사용자는 게시물을 생성, 수정, 삭제, 복구 할 수 있습니다.
- 인증된 사용자는 게시물들을 검색, 필터, 정렬을 통해 조회 할 수 있습니다.
- 인증된 사용자는 생성된 게시물을 열람 할 수 있습니다.

<br>

## 🛠 사용 기술
<br>

<img src="https://img.shields.io/badge/Python-blue?style=plastic&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django Rest Framework-EE350F?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-00979D?style=plastic&logo=MySQL&logoColor=white"/>

<br>

<img src="https://img.shields.io/badge/AWS EC2-FF9900?style=plastic&logo=amazon ec2&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS RDS-527FFF?style=plastic&logo=amazon rds&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=plastic&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Gunicorn-499848?style=plastic&logo=gunicorn&logoColor=white"/>
<img src="https://img.shields.io/badge/NGINX-009639?style=plastic&logo=nginx&logoColor=white"/>

<br>

<img src="https://img.shields.io/badge/Github Actions-2088FF?style=plastic&logo=github actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=plastic&logo=pytest&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=Git&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-grey?style=plastic&logo=github&logoColor=181717"/>

<br>

## 🚀 배포

![SNS deploy structure](https://user-images.githubusercontent.com/83942213/186927642-5a075c5e-d84c-4d56-867a-90ea96afe76d.jpeg)

<img width="458" alt="스크린샷 2022-08-25 오후 3 32 10" src="https://user-images.githubusercontent.com/83942213/186616248-76cec426-286e-4a56-a627-0716c1175290.png">

- 배포 주소는 http://43.200.46.93/ 입니다.
- 비용의 문제로 AWS 인스턴스는 중지상태입니다.
- AWS RDS, Docker-compose, Gunicorn, Nginx를 사용해 AWS EC2서버에 배포했습니다.

<br>

## 💡 ERD
![sns erd](https://user-images.githubusercontent.com/83942213/185592646-079dac3d-687d-42ab-b159-dbd364db6d81.png)

<br>

## 📜 API 명세서

<img width="911" alt="스크린샷 2022-09-20 오전 12 16 51" src="https://user-images.githubusercontent.com/83942213/191052998-76413347-a444-4627-9d41-768b2dbea724.png">

<br>

## 🔗 Task 관리

<img width="1102" alt="스크린샷 2022-08-25 오후 5 51 18" src="https://user-images.githubusercontent.com/83942213/186620407-9fa7d748-0e1d-4167-95ff-f421e6841173.png">


- Github의 <a href="https://github.com/sxxk2/SNS/issues" target="_blank">Issue</a> 와 
<a href="https://github.com/users/sxxk2/projects/5" target="_blank">Projects</a>를 사용합니다.
- issue 생성으로부터 개발을 시작하며 해당 기능을 개발 후 commit시 issue번호를 commit에 남깁니다.
- 명확한 라벨을 사용해 다른 작업자들도 한 눈에 보기 쉽게 구성했습니다.
 
<br>

## 🌱 브랜치 전략

- Github-flow를 사용합니다.
- main에서 파생된 feature 브랜치를 생성해 작업합니다.
- pull request를 통해 main에 병합합니다.
- pull reqeust template를 사용해 작업내용을 공유하고 호출테스트 사진을 첨부합니다.

<br>

## ✨🍰✨ 코드 컨벤션

- pre-commit
- github actions
- Formatter
  - isort
  - black
- Lint
  - flack8

<br>

### 💻 Local
<img width="662" alt="스크린샷 2022-08-19 오후 6 55 20" src="https://user-images.githubusercontent.com/83942213/185594792-dab3b933-9885-423a-a1b7-6f2c36d7af69.png">

- pre-commit 라이브러리를 통해 commit 시 자동으로 스테이징되어있는 코드에 대해 Formatter와 Linter를 실행합니다.
- 통과가 되지않는다면 커밋은 발생하지 않습니다.

<br>

### 🗄 Repository
<img width="1261" alt="스크린샷 2022-08-19 오후 7 16 54" src="https://user-images.githubusercontent.com/83942213/185597932-354cd857-330e-4f83-a372-2042b1035c64.png">

- push시, main 브랜치에 변경점이 있을시 gitahub actions를 통해 코드컨벤션을 체크합니다.
- pull reqeust상태에서 통과가 되지 않는다면 merge는 block 됩니다.

<br>

## ✏️ 커밋 컨벤션

<br>

<img width="242" alt="스크린샷 2022-08-19 오후 8 18 11" src="https://user-images.githubusercontent.com/83942213/185607374-7cae65be-7cd6-4717-b1e9-7b3ee04f9340.png">

- type <br>
Init    : 초기화 <br>
Feat    : 기능추가 <br>
Add     : 내용추가 <br>
Refactor: 리팩토링 <br>
Fix     : 버그 수정 <br>
Style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음) <br>
Docs    : 문서 (문서 추가(Add), 수정, 삭제) <br>
Test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음) <br>
Chore   : 기타 변경사항 (빌드 스크립트 수정 등) <br>

- type : 내용 (#issue번호)의 형식으로 커밋을 남깁니다.
- 필요시 rebase를 활용해 불필요한 커밋을 최소화합니다.
- 커밋 타입과 중복되는 설명을 내용부분에 담지 않습니다. 
- (👍) Refactor : 로그인 기능 리팩토링 (#?)
- (👎) Refactor : 로그인 기능 (#?) 

<br>

## 💾 Pull reuqest 컨벤션

<img width="928" alt="스크린샷 2022-08-19 오후 7 26 25" src="https://user-images.githubusercontent.com/83942213/185613409-2402808f-e57b-4ed2-a49f-c15b36f06450.png">

- pull reuqest template가 .github 디렉토리에 저장되어있어, PR 생성시 자동으로 불러와집니다.
- 해당 PR에 대한 배경지식이 없거나 적은 동료 리뷰어에게 리뷰를 받는다는 전제로 객관적으로 항목들을 작성합니다.
- 작성한 API의 호출 테스트를 사진과 함께 첨부합니다.

<br>

## 👌🏻 API 호출 테스트

<br>

### Account

<br>

- 회원가입 성공 (201)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 03 12" src="https://user-images.githubusercontent.com/83942213/185624259-ea640d9f-4553-4d44-9944-7b207f29f5b7.png">

<br><br><br>

- 회원가입 실패 (400)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 04 40" src="https://user-images.githubusercontent.com/83942213/185624450-8a77ba1b-5ee9-4ea4-8f99-7483c28abee3.png">

- account_name 중복 or email 형식에 맞지 않음

<br><br><br>

- 로그인 성공 (200)
<img width="2121" alt="스크린샷 2022-08-19 오후 10 09 12" src="https://user-images.githubusercontent.com/83942213/185625234-acefa262-b6c6-408f-9081-5836e4c5d873.png">

- JWT 토큰 발급

<br><br><br>

- 로그인 실패 (400)
<img width="2130" alt="스크린샷 2022-08-19 오후 10 10 06" src="https://user-images.githubusercontent.com/83942213/185625381-9af61afd-67f3-4019-8db0-2a70af4b40e5.png">

- 이메일 or 비밀번호 틀림

<br><br><br>

- 로그인 실패 (400)
<img width="2122" alt="스크린샷 2022-08-19 오후 10 30 54" src="https://user-images.githubusercontent.com/83942213/185629834-93519e68-df86-4a69-9d85-b0ed2f039fac.png">

- 삭제된 계정 (is_active = False)

<br><br><br>

- 카카오 토큰 요청 (200)
<img width="2122" alt="스크린샷 2022-08-19 오후 10 14 53" src="https://user-images.githubusercontent.com/83942213/185626483-ec20ec02-befd-443e-8776-173fc6af135c.png">

- 카카오 서버로부터 카카오 토큰 요청

<br><br><br>

- 카카오 로그인or회원가입 성공 (200)
<img width="2121" alt="스크린샷 2022-08-19 오후 10 16 10" src="https://user-images.githubusercontent.com/83942213/185626758-fd90272f-effb-4923-9d46-1f77e02cdaab.png">

- 카카오에서 전달받은 카카오토큰으로 카카오 서버에 유저 정보 요청
- 전달받은 유저의 email값으로 DB 조회 후 있다면 로그인, 없다면 회원가입 후 로그인
- JWT토큰 발급

<br><br><br>

- 카카오 로그인 실패 (200)
<img width="2124" alt="스크린샷 2022-08-19 오후 10 17 22" src="https://user-images.githubusercontent.com/83942213/185626929-c1e61f9e-9837-4552-bc78-6d0a1c82ac29.png">

- 잘못된 카카오 토큰 입력

<br><br><br>

- 회원정보 조회 (200)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 22 52" src="https://user-images.githubusercontent.com/83942213/185628145-122d786c-2cdd-4ec7-81d7-a57d7ca1750b.png">


<br><br><br>

- 회원정보 수정 성공 (200)
<img width="2122" alt="스크린샷 2022-08-19 오후 10 25 09" src="https://user-images.githubusercontent.com/83942213/185628745-b8dcc6b4-e824-46e4-970c-64c974980d09.png">

- id=4계정, 토큰에서의 id값 일치

<br><br><br>

- 회원정보 수정 실패 (403)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 27 24" src="https://user-images.githubusercontent.com/83942213/185629024-9021d25d-c93b-462d-a44d-951450215a30.png">

- id=4 계정의 토큰으로 id=1 계정 정보 수정시 (Permission)

<br><br><br>

- 회원 탈퇴 (soft-delete) 성공 (200)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 28 37" src="https://user-images.githubusercontent.com/83942213/185629329-463853d6-005c-4aa0-a9c4-033c759d840c.png">

- id=4 계정의 토큰으로 id=4 회원 탈퇴시

<br><br><br>

- 회원 탈퇴 복구 성공 (200)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 32 52" src="https://user-images.githubusercontent.com/83942213/185630105-1e16b2d8-733a-4083-a5d2-e37ba82a3065.png">

- is_active = True, deleted_at = None 으로 수정

<br><br><br>

- 회원 탈퇴 복구 실패 (400)
<img width="2121" alt="스크린샷 2022-08-19 오후 10 33 46" src="https://user-images.githubusercontent.com/83942213/185630287-f7ebd6d4-4461-4d20-85d8-06ba38c637fc.png">

- 탈되되지 않은 사용자의 값으로 탈퇴복구
- is_active = True 일 시

<br><br><br><br><br>

### Post

<br>

- 게시물 생성 성공 (201)
<img width="2124" alt="스크린샷 2022-08-19 오후 10 35 53" src="https://user-images.githubusercontent.com/83942213/185630903-19881b68-e9a2-4d4a-baf1-b1d3d6e5ad67.png">

<br><br><br>

- 게시물 수정 성공 (200)
<img width="2122" alt="스크린샷 2022-08-19 오후 10 39 39" src="https://user-images.githubusercontent.com/83942213/185631369-5db39553-3d7e-4dd1-bb8b-dbd7e8e484b1.png">

- 게시물 id=36의 작성자id=4, 토큰과 일치
- 입력받은 컬럼들과 함께 updated_at = now 으로 변경

<br><br><br>

- 게시물 수정 실패 (403)
<img width="2122" alt="스크린샷 2022-08-19 오후 10 41 59" src="https://user-images.githubusercontent.com/83942213/185631833-e7cbf5dc-664d-40b0-9f54-df9a0c431805.png">

- 게시물 id=35의 작성자id=2, 토큰의 계정 id=4 (Permission)

<br><br><br>

- 게시물 삭제(soft-delete) 성공 (200)
<img width="2125" alt="스크린샷 2022-08-19 오후 10 45 48" src="https://user-images.githubusercontent.com/83942213/185632637-1ce7dc18-9f7e-44a2-aee9-364898df53a4.png">

- 게시물 id=36의 작성자id=4, 토큰과 일치
- is_deleted = True, deleted_at = now 으로 변경

<br><br><br>

- 게시물 삭제 실패 (403)
<img width="2124" alt="스크린샷 2022-08-19 오후 10 48 42" src="https://user-images.githubusercontent.com/83942213/185633213-e18b253a-b026-4a19-9a1f-e88b43e239f2.png">

- 게시물 id=35의 작성자id=2, 토큰의 계정 id=4 (Permission)

<br><br><br>

- 게시물 삭제 실패 (400)
<img width="2123" alt="스크린샷 2022-08-19 오후 10 53 41" src="https://user-images.githubusercontent.com/83942213/185634835-c23a3b66-3157-4900-96e9-9e3eb76d7bb6.png">

- is_deleted = True 일 시

<br><br><br>

- 게시물 삭제 복구 성공 (200)
<img width="2124" alt="스크린샷 2022-08-19 오후 10 50 38" src="https://user-images.githubusercontent.com/83942213/185633646-d501ac83-0f6f-4dcf-947c-5ff7420ea496.png">

- 게시물 id=36의 작성자id=4, 토큰과 일치
- 이미 삭제된 게시물 ( is_deleted = True ) 일 시
- is_deleted = False, deleted_at = None 으로 변경

<br><br><br>

- 게시물 삭제 복구 실패 (400)
<img width="2126" alt="스크린샷 2022-08-19 오후 11 03 44" src="https://user-images.githubusercontent.com/83942213/185636037-15e1e04d-ff0f-4bbd-84f8-2599ec83deac.png">

- 게시물 id=35의 작성자id=2, 토큰의 계정 id=4 (Permission)

<br><br><br>

- 게시물 복구 실패 (400)
<img width="2123" alt="스크린샷 2022-08-19 오후 11 04 44" src="https://user-images.githubusercontent.com/83942213/185636260-7d3446cb-4aa3-4a1b-8fb3-4165e963c6be.png">

- is_deleted = False 일 시 

<br><br><br>

- 게시물 리스트 조회 (200)
<img width="2124" alt="스크린샷 2022-08-19 오후 11 18 34" src="https://user-images.githubusercontent.com/83942213/185638863-c33711ae-bea7-4c21-ac67-a55d89fae126.png">

쿼리파라미터
- tag : 게시물의 tag값으로 조회, ","을 구분으로 다중값 입력 가능
- search : 제목(title) 혹은(or) 내용(content) 컬럼의 값을 검색
- sort : 정렬, recent=최신순, most_viewd=조회수 높은순. ( default = recent )
- offset:limit : offset:offset+limit. ( default offset = 10 )


<br><br><br>

- 게시물 단건 조회 성공 (200)
<img width="2124" alt="스크린샷 2022-08-19 오후 11 28 42" src="https://user-images.githubusercontent.com/83942213/185641033-e0f656dc-1405-4220-8414-e7ecfd1a1c3d.png">

- 게시물 조회 성공시 views(조회수) 1 증가

<br><br><br>

- 게시물 단건 조회 실패 (404)
<img width="2120" alt="스크린샷 2022-08-19 오후 11 31 08" src="https://user-images.githubusercontent.com/83942213/185641691-e3786762-cb88-481d-83e5-c0f0657622ff.png">

- 없는 게시물


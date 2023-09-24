# TrackProject_2_YoungguKang

## 프로젝트 미완성 
- modules 정상작동 X

환경 및 버전

언어

Python: 3.9.13

라이브러리

Django: 4.2.5 <br>
djangorestframework: 3.14.0 <br>
drf-spectacular: 0.26.4 <br>
psycopg2-binary: 2.9.7<br>
gunicorn: 21.2.0<br>

클라우드

backend-server: ubuntu 20.04<br>
db-server: ubuntu 20.04<br>

도커

Docker: 24.0.2<br>
backend-image: python-3.11-alpine<br>
db-image: postgresql-13<br>



### 1. 백엔드 DB 설계

- [x] Post
- [x] Follow

### 2. 백엔드 API 개발

- 유저
  - [x] 사용자 본인을 제외한 전체 사용자 목록을 확인할 수 있다.
- 게시글
  - [x] 사용자는 모든 게시글을 볼 수 있다.
  - [x] 사용자는 게시글을 올릴 수 있다.
  - [ ] 사용자는 본인의 게시물을 모아볼 수 있다.
  - [ ] 사용자는 본인의 게시물을 수정하거나, 삭제할 수 있다.
- follow
  - [x] 사용자는 다른 사용자를 follow(unfollow)할 수 있다.
  - [x] 사용자는 follow한 사람들 목록을 확인할 수 있다.
  - [ ] 사용자는 나를 follow하고 있는 사람들 목록을 확인할 수 있다.
  - [ ] 사용자는 follow한 사람들이 올린 게시물을 모아볼 수 있다.

### 3. 더미데이터 추가

- [ ] 사용자 5명 이상
- [ ] 사용자당 게시글 3개 이상

### 4. 테스트 코드 작성

- [ ] 전체 사용자 목록에서 자신을 제외한 목록이 잘 나오는지 테스트
- [X] 모든 게시물이 출력되는지 테스트
- [ ] 본인의 게시물만 수정, 삭제가 가능한지 테스트
- [ ] follow / unfollow 기능이 잘 작동하는지 테스트
- [ ] follow한 사람들이 올린 게시물을 잘 확인할 수 있는지 테스트
- [ ] 기타 테스트가 필요한 내용 테스트

### 5. 배포

- [ ] runserver, gunicorn 등을 사용해서 배포
- [ ] 어디서든 API 호출이 가능하도록 백엔드 서버를 클라우드 서비스를 통해 배포

### 6. CICD Pipeline 작성

- [x] Github actions로 구현
- [ ] push가 됐을 때, 테스트 코드를 실행하여, 테스트가 정상 작동하는지 확인하고, 정상 작동하면, 서버에 새 버전을 배포

### 백엔드 서버 분리

- [x] 백엔드 서버와 DB 서버를 물리적으로 분리

### 도커 컨테이너로 배포

- [ ] docker image를 이용한 container로 배포

### 로드밸런서를 통해 배포

- [ ] 인스턴스에 직접 접근하는 대신 로드밸런서를 통해 API를 호출할 수 있도록 배포 >> 

### CICD Pipeline 작성

- [x] PR이 있을 때, 테스트 코드를 실행하여, 테스트가 정상 작동하는지 확인

### 7. terraform 작성

- [x] 배포 및 운영에 필요한 모든 인프라를 terraform으로 관리한다.

### 8. multi-stage 구성

- [x] production과 staging 환경을 별도로 구성한다.
- [ ] terraform 으로 손쉽게 각 환경을 구성(apply)하고, 폐기(destroy)할 수 있다.

### 9. k8s로 배포

- [ ] 서비스를 k8s로 배포한다.

### 10. 백엔드 서버 분리

- [x] 백엔드 서버와 DB 서버를 물리적으로 분리

---

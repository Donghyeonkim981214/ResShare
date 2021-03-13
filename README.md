# Restaurant-Share

## 0. 목차
1. 프로젝트 소개
  * Restaurant-Share
  * 개발환경
2. 기능소개
  * 기본 기능
  * 로그인 후 가능한 기능
3. 개발 완료
  * 수정
  * 확장
4. 개발 중
  * 해결할 이슈
  * 보완할 기능
5. 끝맺음
  * 소감
  * Licence

## 1. 프로젝트 소개
* Restaurant-Share
  본 프로젝트는 'Django 한그릇 뚝딱'(문범우 지음, 비제이리퍼블릭)의 chapter 3_ 맛집 공유 사이트 만들기 내용을 베이스로 하여 해당 프로젝트를 수정 및 확장한 프로젝트입니다.
  사용자는 음식점을 추가할 수 있고 리뷰와 평점을 공유할 수 있습니다. 또 음식점 리스트를 체크하여 자신의 맛집 리스트를 메일로 보내 공유할 수 있습니다.   
  Web url: http://tunatest.pythonanywhere.com/
* 개발환경
  * os: windows10
  * editor: visual studio code
  * language: python 3.7
  * backend: django(3.1.7)
  * database: sqlite3
  * frontend: html, css
  * deploy: pythonanywhere

## 2. 기능 소개
  * 기본기능
  로그인하지 않고 사용할 수 있는 기능은 다음과 같습니다.
   1. 음식점 상세 설명보기
   2. 음식점 리스트 메일로 공유하기

  * 로그인 후 가능한 기능
   1. 음식점 추가 및 수정
   2. 카테고리 추가 및 수정
   3. 리뷰 작성

## 3. 개발 완료
* 수정   
  1. FBV -> CBV: 'Django 한그릇 뚝딱에서는 모든 view가 Function bsed view로 설계되었다. 이를 Class based view로 전환하면서 Django에서 제공하는 다양한 generic view를 연습하였다.
  2. template: 'Django 한그릇 뚝딱에서는 필요한 template파일이 개별적으로 설계되었다. 이를 template상속을 통해 base.html을 바탕으로 template파일을 효율적으로 설계 및 확장할 수 있도록 하였다.
* 추가   
  1. users app을 추가하여 사용자의 회원가입, 로그인 등의 기능을 추가하였다. 또 로그인한 사용자만이 음식점을 추가하고 리뷰할 수 있는 등 비로그인 사용자와의 사용가능한 기능의 범위를 다르게 설정하였다.   
  2. reviews app을 추가하여 로그인한 사용자가 음식점에 관한 평가와 평점을 작성할 수 있도록 추가하였다. 또 음식점 상세설명에서 사용자들이 남긴 review들을 볼 수 있게 했으며, 평점의 평균도 같이 나타내 주었다.   

## 4. 개발 중
  * 해결할 이슈   
    1. 사용자 개별 서비스 제공: 현재 사용자 별로 카테고리 및 수집 음식점이 분리가 되지 않았음.
    2. 음식점에 관한 별개의 app이 필요: 현재 shareRes app에 category와 restaurant model이 같이 설계되어 있음. 분리가 필요.
  * 보완할 기능   
    1.  음식점 추가에 대한 기능 보완 필요: 사용자가 직접 정보를 입력하는 것이 아닌 검색사이트에 나와있는 음식점의 정보를 불러와 추가하는 방향으로 설계.
    
## 5. 끝맺음
* Licence   
이 repository 의 내용은 'Django 한그릇 뚝딱'(문범우 지음, 비제이리퍼블릭)의 chapter 2_ ToDoList 내용을 토대로 수정 및 보완한 내용입니다.
해당 repository는 저자님께 직접 허가를 구하고 올린 것이며 <Django 한그릇뚝딱>에 대한 모든 source code에 대한 권한은 '문범우'님에게 있습니다.
코드 출처:
https://github.com/doorBW/Django_with_PracticeExamples

# 🦁 아이디어톤 공유 사이트 
![img](/DIT/static/img/슬라이드1.JPG)

- 동국대학교 멋쟁이사자처럼 아이디어톤 공유 사이트.
- 동국대학교 멋쟁이사자처럼 8기의 중앙 아이디어톤과 해커톤을 준비하기 위한 아이디어 나눔의 장입니다.
  
<br>

# 📖 Contents
[:one: Specification](#one-specification) <br>
[:two:​ ERD](#two-erd)<br>
[:three:​ Flow Chart](#three-flow-chart)<br>
[:four:​ Server Architecture](#four-server-architecture)<br>
[:five: 기능 명세](#five-기능-명세)<br>
[:siv: Deploy Fundamentals](#six-deploy-fundamentals)<br>
<br>

## ​:one:​ Specification

<table class="tg">
<tbody>
  <tr>
    <td><b>Architecture</b></td>
    <td>MVC</td>
  </tr>
   <tr>
    <td><b>DB</b></td>
    <td>MySQL</td>
  </tr>
   <tr>
    <td><b>Framework</b></td>
    <td>Django, DRF</td>
  </tr>
   <tr>
    <td><b>Deployment</b></td>
    <td>AWS EC2, RDS, Docker, Docker-compose</td>
  </tr>
<tr>
    <td><b>Other Tool</b></td>
<td>Notion</td>
</tr>
</tbody>
</table>

<br>

## :two:​ ERD
<img src='/imgs/ERD.png' width="50%" height="50%">
<br>

## :three:​ Flow Chart
<img src='/imgs/FC.png' width="50%" height="50%">
<br>

## :four:​ Server Architecture
<img src='/imgs/SA.png' width="50%" height="50%">
<br>

## :five:​ 기능 명세
<table class="tg">
<tbody>
  <tr>
    <td><b>메인페이지</b></td>
    <td> - 작성된 포스트 목록 리스트 확인</td>
  </tr>
   <tr>
    <td><b>로그인/로그아웃</b></td>
    <td>
      - 사전에 운영진에 의해 등록된 사용자만 활용 가능.<br>
      - 기본 로그인, 로그아웃 기능.
      </td>
  </tr>
   <tr>
    <td><b>포스트</b></td>
    <td>
      - 포스트 생성: 제목, 내용, 첨부파일 작성하고 생성.<br>
      - 포스트 수정: 사용자에 한해 detail로 들어가 수정 가능.<br>
      - 포스트 삭제: 사용자에 한해 detail로 들어가 삭제 가능.<br>
      - 포스트 읽기: 제목, 내용, 첨부파일 확인가능.
    </td>
  </tr>
   <tr>
    <td><b>댓글</b></td>
    <td>
      - 댓글 생성: 원하는 포스트에 댓글을 작성.<br>
      - 댓글 삭제: 본인이 작성자인 경우 삭제.<br>
      - 댓글 확인: 포스트 아래에 댓글을 보여줌.
    </td>
  </tr>
  <tr>
    <td><b>좋아요</b></td>
    <td>
      - 포스트에 대해 좋아요 생성/취소.<br>
    </td>
  </tr>
</tbody>
</table>

<br>

## ​:six:​ Deploy Fundamentals
```
💡 Docker를 활용한 배포와 DRF 개발을 위해 필요한 기초 지식 정리 내용
```
[1. REST](https://www.notion.so/thediaryofyj/6-28-REST-d5c74be70008443f9c58c2f9725dfd8c)<br>

[2. WS와 WAS의 차이, Uwsgi와 Nginx](https://www.notion.so/thediaryofyj/6-23-WS-WAS-Uwsgi-Nginx-e03f1b6e0b704e66976c5078c741f03e)<br>

[3. Docker](https://www.notion.so/thediaryofyj/6-24-Docker-c15eeed38d52455a8317fd0f8de52733)<br>

[4. Docker을 활용한 배포](https://www.notion.so/thediaryofyj/7-11-7-13-Docker-6d481f94231a4d28ad69cead7558f2ee)<br>

<br>

## 👣 Footprints of Development
<a href="https://www.notion.so/thediaryofyj/Restframework-6ddc4152bfe747b8942c0ed86ee397c6">
 <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&link=https://www.notion.so/thediaryofyj/Restframework-6ddc4152bfe747b8942c0ed86ee397c6"/>
</a> 

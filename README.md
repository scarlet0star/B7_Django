# B7_Django
![stack](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQ5z3f%2FbtrJ8nx28A7%2F1aL7dMH5ZE2DFTeDYJfzTK%2Fimg.png)<br>
중고거래 사이트들을 참고하여 만든 Django / nginx / mysql 클론 웹사이트입니다.<br>
이 repo는 백엔드 파트입니다.<br>
https://www.notion.so/Be-Se7en-ca50c20f58bc431baa4ebbd9313c5de4

자세한 내용은 위에 담겨있으니 가볍게 서술하겠습니다.

## 역할 분담

김성광 : Office App + Chart.js / nginx conf / docker-compose / AWS EC2, LoadBalancer, ACM, Route 53 + git page 연동<br>
구병진 : 게시글 (Article) App<br>
박지홍 : 채팅기능 구현 (구현 완료 시 추가 기능 구현)<br>
이현식 : 상품(Product) App<br>
임라온 : User App<br>

backend : https://lucedude.link<br>
git page repo: https://github.com/scarlet0star/scarlet0star.github.io

## 주요 기능
배포된 웹페이지 : https://scarlet0star.github.io 실제로 배포되었기 때문에 웹으로 접속가능.<br>
상품들과 관련된 기능들 : 기본적인 CRUD , 북마크 ,피드 페이지 구현, 끌어올리기, 이미지 삽입, 카테고리 구현<br>
simple JWT를 이용한 로그인 구현<br>
Chart.js를 통한 간단한 통계 구현

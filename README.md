# TeamProject

---

## Festa-Crawling

----

> [festa](https://festa.io/)홈페이지에서 사용자가 원하는 키워드를 등록한 후, 등록한 키워드가 새롭게 포스팅되면 이메일로 알림을 주는 서비스

#### URL

http://festa.s3-website.ap-northeast-2.amazonaws.com/

### 프로젝트 참가인원

----



| Backend              | Front  |
| -------------------- | ------ |
| 박홍빈,이도현,오형근 | 이철환 |

### 프로젝트 선정 이유

-----

[festa](https://festa.io/)홈페이지에는 개발자, 페스티벌 등 등의 컨퍼런스가 개최됩니다.

개발자라면 새로운 기술, 본인이 모르는 기술,  또는 부족한기술에 대해서 열린 마음으로 관심을 갖어야한다는 생각으로 컨퍼런스를 탐색하기 위해 [festa](https://festa.io/)홈페이지를 주기적으로 접속하여 확인했습니다.

그러다보니 번거로움을 느꼈고 이러한 부분들을 조금 더 편리하게 알림을 받아보고 싶어서 선정하게 되었습니다.

그리고 참가인원 모두 개인 프로젝트는 많이 진행해보았기 때문에, 협업을 통해서 백엔드와 프론트엔드간에 커뮤니케이션, github사용법, 문서화작업 등에 대해서 익숙해지고자 협업하게 되었습니다.

### 사용기술

-----

- Backend
  - 배포
    - AWS(EC2, Secrets manager, S3, RDS)
    - 웹 애플리케이션 서버: Gunicorn
    - 웹서버: Nginx
    - Docker
  - 크롤링
    - Scrapy
    - Selenium
  - Framework
    - Django-Rest-Framework
  - Database
    - PostgreSQL
- Frontend
  - HTML5
  - CSS3
  - Javascript
  - slick-carousel
  - query-string
  - styled-components
  - uuid
  - axios
  - React
    - react-router-dom
    - react-error-boundary
    - react-slick
    - react-loader-spinner
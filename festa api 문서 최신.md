### 요약

---

**localhost:8000/{parameter}**

--- 로그인/로그아웃/사용자 생성 ---

1. localhost:8000/members/auth-token/ : 유효한 사용자가 아이디/비번을 지급시 토큰 반환. **POST**

2. localhost:8000/members/check-user/: 사용자의 아이디가 존재하는지 확인. **GET**

3. localhost:8000/members/create-user/ : 사용자 생성. **POST**

4. localhost:8000/members/logout-user/: 사용자 로그아웃(로그인시 발급받은 토큰 삭제). **GET**



--- 모든 리스트 받기(유료/무료/외부이벤트 구분)/특정 이번트의 내용 보기/ 키워드 등록 ---

5. localhost:8000/festalist/ : 모든 리스트 받기(유료/무료/외부이벤트 구분) **GET**
   1. category=(pay, free,exterior)&page=(int)&size=(int)로 정보를 구별하여 얻을 수 있음
6. localhost:8000/festalist/[int:pk]/ :특정 이벤트의 내용 보기 **GET**
7. localhost:8000/festalist/keyword/ : 키워드 등록 **POST**
8. localhost:8000/festalist/keyword/ :  받아오기 **GET** 
9. localhost:8000/festalist/keyword/[int:pk]/  : 사용자의 키워드 삭제**DELETE**



--- AuthToken을보내는 방식 ---

`http http://127.0.0.1:8000/hello/ 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'`





#### POST 

---

|      parameter       | Token required |       request body        |                  Information                   |
| :------------------: | :------------: | :-----------------------: | :--------------------------------------------: |
| members/auth-token/  |       χ        |      email, password      | 유효한 사용자가 아이디/비번을 지급시 토큰 반환 |
| members/create-user/ |       χ        | username, password, email |                  사용자 생성                   |
|  festalist/keyword/  |      *o*       |          keyword          |         특정 사용자 새로운 키워드 추가         |



### GET 

---

|            parameter            | Token required | request body |                 Information                  |
| :-----------------------------: | :------------: | :----------: | :------------------------------------------: |
|      members/logout-user/       |      *o*       |      χ       |     사용자 로그아웃. 소지하던 토큰 삭제      |
| members/check-user?email=이메일 |       χ        |     *X*      |  로그인시 사용자의 아이디가 존재하는지 확인  |
|       festalist/[int:pk]/       |       χ        |      χ       |               특정 이벤트 반환               |
|       festalist/keyword/        |      *o*       |      χ       | 특정 사용자가 저장한 모든 키워드 가지고 오기 |
|           festalist/            |       χ        |     *X*      |               모든 이벤트 표시               |
|        members/get-user/        |       o        |      x       |  사용자의 이메일, 아이디 정보를 가지고온다   |



### DELETE 

---

|          parameter           | Token required | request body |     Information      |
| :--------------------------: | :------------: | :----------: | :------------------: |
| /festalist/keyword/[int:pk]/ |      *o*       |      χ       | 사용자의 키워드 삭제 |





### Request/Response  예시

#### 1.  localhost:8000/members/auth-token/ 				(POST)

> **유효한 사용자가 로그인시  Token과 사용자 정보 반환**
>
> request Header 에 AuthToken 필요:
>
> - χ
>
> request body 에 넣는 데이터:
>
> - email 
> - password

사용자 아이디/비밀번호가 **유효할** 경우:(payload랑 반환값 변경)

```json
---Request---
localhost:8000/members/auth-token/
body message에 유효한 데이터를 넣어서 보낼경우
{
  "email":"test@test.com",
  "password":"1234"
}


---Response 에 token값과 사용자 정보 반환---
{
    "token": "7214b803fdba12116b4374edb7c8ad73f8ce90de",
    "user": {
        "id": 1,
        "email": "test@test.com",
        "password": "pbkdf2_sha256$150000$e7JgXcUlV8S9$JZs64U93a4N9/0qxoOI7pinWkEN0w7vKxgz0m2lzTx0="
    }
}
```



사용자 아이디/비밀번호가 **유효하지 않을경우**:

```json
---Request---
localhost:8000/members/auth-token/
body message에 유효하지 않은 데이터를 넣어서 보낼경우
{
  "email":"errortest@test.com",
  "password":"1234"
}


---Response 에서 error 메시지 반환---
{
	"detail": "자격 인증데이터(authentication credentials)가 정확하지 않습니다."
}
```



#### 2. localhost:8000/members/check-user?email=이메일 				(GET)​ 

> **사용자의 아이디가 존재하는지 확인**
>
> request Header 에 AuthToken 필요:
>
> - χ
>
> request body 에 넣는 데이터:
>
> - X
> - 쿼리스트링으로 email 이 있는지 없는지 확인

사용자 아이디가 **존재할 경우**:

```json
---Request---
localhost:8000/members/check-user?email=test@test.com


---Response---
{
    "isExist": true
}
```

사용자 아이디가 **존재하지 않을경우**:

```json
---Request---
localhost:8000/members/check-user/email=testtest22@test.com


---Response---
{
    "isExist": false
}
```



#### 3. localhost:8000/members/create-user/  				(POST)

> **사용자 생성**
>
> request Header 에 AuthToken 필요:
>
> - χ
>
> body message 에 넣는 데이터:
>
> - password
> - email (unique 하지 않음. 추후 수정)

새로운 사용자 생성 **성공**:

```json
---Request---
localhost:8000/members/create-user/ 
body message
{
	"email":"festa@naver.com",
	"password":"1234"
}


--Response (데이터베이스에 이도현이라는 username이 존재하지 않을경우)--
{
    "user": {
        "email": "festa@naver.com",
        "password": "1234"
    },
    "detail": "festa@naver.com로 새로운 계정을 생성하셨습니다"
}
```



새로운 사용자 생성 **실패**:(데이터베이스이 에미 사용자가 존재할 경우)

```json
---Request---
localhost:8000/members/create-user/ 
body message
{
	"email":"festa@naver.com",
	"password":"1234"
}


---Response---
{
    "email": [
        "사용자의 이메일은/는 이미 존재합니다."
    ]
}
```



#### 4. localhost:8000/members/logout-user/ 				(GET)

> **사용자 로그아웃시 소지하고 있던 AuthToken 삭제**
>
> request Header 에 AuthToken 필요:
>
> - ○
>
> body message에 넣는 데이터:
>
> - χ

해당 url 로 AuthToken을 넣어서 보내면 로그아웃이 된다.

옳바른 토큰값을 **넣어줄경우**

```json
---Request---
localhost:8000/members/logout-user/ 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'


---Response---
{
    "detail": "로그아웃 하셨습니다."
}
```

옳바른 토큰값을 넣어주지 **않을 경우**

```json
---Request---
http localhost:8000/members/logout-user/ 'Authorization: Token 잘못된토큰값'


---Response---
{
    "detail": "토큰이 유효하지 않습니다."
}
```





### 5. localhost:8000/festalist/				(GET) 

> **모든 이벤트를 유료/무료/외부이벤로 나누어서 반환**
>
> request Header 에 AuthToken 필요:
>
> - Optional. 넣을경우 사용자 정보 반환
>
> body message 에 넣는 데이터:
>
> - χ

url로 request 를 보낼시 다음 get 요청을 보낼 수 있다. (category=category&page=page&size=size)

category에 요청할 수 있는 정보는 다음과 같다.

​	1. pay --> 유료

​	2. free --> 무료

​	3. exterior -->외부 이벤트

size는 기본적으로 30이다.

count 는 전체 개수가, next에는 다음 페이지, previous에는 이전 페이지의 주소가 담겨있다.

주의할것은 **배열 안에 객체 형식으로 저장되어있다.**

```json
---Request---
localhost:8000/festalist/


---Response---
{
    "count": 745,
    "next": "http://127.0.0.1:8000/festalist/?page=2",
    "previous": null,
     "results": [
        {
            "id":"이벤트 아이디",
            "title":"이벤트 이름",
            "host":"이벤트 주최자",
            "date":"이벤트 날짜",
            "content":"이벤트 내용",
            "apply":"이벤트 신청 가능 상태: 외부등록/이벤트 종료/이벤트 신청",
            "tickets":"티켓 가격",
            "link":"외부이벤트 링크",
            "image":"이벤트 사진"
        },

        {
            "id":"이벤트 아이디",
            "title":"",
            "host":"",
            "date":"",
            "content":"",
            "apply":"",
            "tickets":"",
            "link":"",
            "image":""
        }
	]
}
```

get으로 param을 보내는 경우는 다음과 같다.

```json
---Request---
localhost:8000/festalist/?category=pay&page=3&size=20


---Response---
{
    "count": 328,
    "next": "http://127.0.0.1:8000/festalist/?category=pay&page=4&size=20",
    "previous": "http://127.0.0.1:8000/festalist/?category=pay&page=2&size=20",
    "results": [
        {
            "id":"이벤트 아이디",
            "title":"이벤트 이름",
            "host":"이벤트 주최자",
            "date":"이벤트 날짜",
            "content":"이벤트 내용",
            "apply":"이벤트 신청 가능 상태: 외부등록/이벤트 종료/이벤트 신청",
            "tickets":"티켓 가격",
            "link":"외부이벤트 링크",
            "image":"이벤트 사진"
        },
        {
            "id":"이벤트 아이디",
            "title":"이벤트 이름",
            "host":"이벤트 주최자",
            "date":"이벤트 날짜",
            "content":"이벤트 내용",
            "apply":"이벤트 신청 가능 상태: 외부등록/이벤트 종료/이벤트 신청",
            "tickets":"티켓 가격",
            "link":"외부이벤트 링크",
            "image":"이벤트 사진"
        },
    ]
}
   
```





### 6. localhost:8000/festalist/[int:pk]/			(GET)

> **존재하는 모든 이벤트 중 특정 이벤트 반환**
>
> [int:pk] 는 쿼리스트링을 의미하는데, **숫자**이어야 한다
>
> request Header 에 AuthToken 필요:
>
> - χ
>
> body message 에 넣는 데이터:
>
> - χ

localhost:8000/festalist/4/ 로 request 를 보내면 다음과 같은 데이터가 반환된다.

[int:pk]에 4가 오고, 여기서 4는 데이터베이스에서 이벤트의 아이디가 4번이라는걸 의미한다.

```json
---Request---
localhost:8000/festalist/4/


---Response---
{
    "listDetail": {
      	"id":4,
        "title": "코딩 도장 #17",
        "host": "달랩",
        "date": "2020년 02월 18일 (화)\n오후 07:30 - 오후 09:30",
        "content": "<div class=\"UserContentArea-sc-1w8buon-0 kUPCzS\"><p>일주일에 하나씩 가벼운 마음으로 코드를 작성합니다.</p>\n<p>누가 떠밀지 않아도 스스로 자라길 원하는 사람들의 모임입니다.</p>\n<p>2시간 동안 함께 간단한 문제를 풀면서 프로그래밍 스킬을 수련합니다.</p>\n<p>규칙은 단 하나입니다. 짝 프로그래밍을 하는 거죠.</p>\n<p> </p>\n<p>GitHub 저장소: <a href=\"https://github.com/dal-lab/coding-dojo\" target=\"_blank\">https://github.com/dal-lab/coding-dojo</a></p>\n<p> </p>\n<p> </p></div>",
        "apply": "이벤트 종료",
        "tickets": "(코딩 수련, ₩5,000)",
        "link": "",
        "image": "https://cf.festa.io/img/2020-2-18/0696da71-0bdd-4b95-bf39-31ce2d0c023c.jpeg"
    }
}
```



잘못된 이벤트 아이디를 보낼경우

```json
---Request---
localhost:8000/festalist/555555555/


---Response---
{
    "detail": "잘못된 이벤트 입니다"
}
```



### 7. localhost:8000/festalist/keyword/ 		(POST) 

> **특정 사용자 새로운 키워드 추가**
>
> [int:pk] 는 쿼리스트링을 의미하는데, **숫자**이어야 한다.
>
> request Header 에 AuthToken 필요:
>
> - O
>
> body message 에 넣는 데이터:
>
> - keyword --> 사용자가 등록할 키워드

사용자 키워드 등록

```json
---Request---
localhost:8000/festalist/keyword/
body message
{
	"keyword":"자바스크립트"
}



---Response---
{
    "data": {
        "keyword": "자바스크립트"
    }
}
```

잘못된 토큰을 전달할경우 

```json
---Request---
localhost:8000/festalist/keyword/


---Response---

{
    "detail": "토큰이 유효하지 않습니다."
}
```



### 8. localhost:8000/festalist/keyword/  		(GET) 

> **특정 사용자의 모든 키워드 불러오기**
>
> [int:pk] 는 쿼리스트링을 의미하는데, **숫자**이어야 한다.
>
> request Header 에 AuthToken 필요:
>
> - O
>
> body message 에 넣는 데이터:
>
> - χ
>
> 사용자가 등록한 키워드가 없으면 빈배열을 반환한다 :white_check_mark:

옳바른 토큰을 넣어서 보낼경우

```json
---Request---
localhost:8000/festalist/keyword/


---Response---
{
    "keywords": [
        {
          	"id":1
            "keyword": "Java"
        },
      	{
          	"id":2
            "keyword": "JavaScript"
        }
    ]
}
```

잘못된 토큰을 전달할경우 

```json
---Request---
localhost:8000/festalist/keyword/


---Response---

{
    "detail": "토큰이 유효하지 않습니다."
}
```



### 9. localhost:8000/festalist/keyword/[int:pk]/  		(DELETE)

---

> **특정 사용자의 키워드 삭제**
>
> [int:pk] 는 쿼리스트링을 의미하는데, **숫자**이어야 한다.
>
> request Header 에 AuthToken 필요:
>
> - O
>
> body message 에 넣는 데이터:
>
> - χ

```json
---Request---
localhost:8000/festalist/keyword/13/


---Response--- status:200
{
    "data": "데이터를 삭제하였습니다."
}
```





### 10. localhost:8000/members/get-user/

---

>**사용자의 username, 이메일 가져오기**
>
>request Header 에 AuthToken 필요:
>
>- O
>
>body message 에 넣는 데이터:
>
>- χ

토큰을 넣을경우 사용자의 정보도 같이 반환해준다

```json
"user": {
        "id": 25,
        "username": "newuser123",
        "email": "newuser123@naver.com"
    },
}
```


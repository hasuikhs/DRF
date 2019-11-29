# JWT-Authentication

## JWT(JSON Web Token) 이란 ?

- JSON Web Token은 웹표준으로서 두 개체에서 JSON 객체를 사용하여 가볍고 자가수용적인(self-contained) 방식으로 정보를 안전성 있게 전달해준다.
- **수많은 프로그래밍 언어에서 지원**
- JWT는 필요한 모든 정보를 자체적으로 지니고 있다. JWT에서 발급된 토큰은 토큰에 대한 기본정보, 전달 할 정보 그리고 토큰이 금증됐다는 것을 증명해주는 signature를 포함하고 있다.

[JWT 더 자세한 정보](http://throughkim.kr/2017/03/14/Jwt/)

[자세한 정보 2](https://tansfil.tistory.com/58)

- `pip install list`
  
    ```bash
    $ pip install django
    $ pip install djangorestframework
    $ pip install django-cors-headers
    $ pip install djangorestframework-jwt
    ```

## 1. 인증 과정

### 1.1 로그인 화면

- DRF에서 제공하는 화면

![image-20191128214518621](README.assets/image-20191128214518621.png)

### 1.2 로그인

![image-20191128214550270](README.assets/image-20191128214550270.png)

- 로그인 결과 반환값

![image-20191128214618733](README.assets/image-20191128214618733.png)

- 포스트맨에서의 로그인 테스트(성공시)

  ![image-20191128214904675](README.assets/image-20191128214904675.png)

- 포스트맨에서의 로그인 테스트(실패시)

  ![image-20191128215038935](README.assets/image-20191128215038935.png)

### 1.3 토큰 활용 방법

![image-20191128215359300](README.assets/image-20191128215359300.png)

- `headers`에 `Authorization`에 토큰값을 넣는다.
  - 토큰값을 넣는데 맨 앞에 `JWT`를 붙이자
- 이제 `JWT`를 이용해서 사용자의 정보를 인증하여 정보를 가져올 수 있다.
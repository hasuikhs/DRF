# Project_HF

- Django를 이용한 REST API 서버 만들기

### 0. 사전 준비

#### 0.1 Module 설치

```bash
$ pip install django
$ pip install djangorestframework
$ pip install django-rest-swagger
```

#### 0.2 Project 생성

```bash
$ djagno-admin startproject config .
```

#### 0.3 App 생성

```bash
$ python manage.py startapp accounts
$ python manage.py startapp articles
```

#### 0.4 `config/settings.py` 설정

```python
INSTALLED_APPS = [
	...
    'rest_framework',
    'rest_framework_swagger',
    'accounts',
    'articles',
]

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

...

AUTH_USER_MODEL = 'accounts.User'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### 0.5 `accounts/models.py`

```python
from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blanck=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
```


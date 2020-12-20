## Keycloak + Django REST Framework

Library for DRF - Keycloak integration using OpenId Connect: 
https://github.com/ByteInternet/drf-oidc-auth
 
#### Installation

```
$ git clone https://github.com/olechanastazja/keycloak_django.git
```

Keycloak + PostgreSQL
```
$ cd keycloak_django
# docker-compose up
```

Keycloak should be ready to user on port 8080, example login and password for admin user are in docker-compose

Django + SQLite3

```
$ virtualenv venv/

$ source venv/bin/activate

$ pip install -r requirements.txt

$ cd poleval_auth 

$ python3 manage.py migrate 

$ python3 manage.py runserver
```

The DRF application in available on port 8000. It'a a backend application only. To check if it's working as expected
you can user Postman or curl.

   

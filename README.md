## Keycloak + Django REST Framework


Biblioteka, której używam do integracji z Keycloak z wykorzystaniem OpenId Connect: 
https://github.com/ByteInternet/drf-oidc-auth
 
#### Instalacja

```
$ git clone https://github.com/olechanastazja/keycloak_django.git
```

Keycloak + PostgreSQL
```
# docker-compose up
```

Keycloak będzie dostępny na porcie 8080, hasło i login dla admina są w docker-compose

Django + SQLite3

```
$ virtualenv venv/

$ source venv/bin/activate

$ pip install -r requirements.txt

$ cd poleval_auth/poleval_auth & python3 manage.py migrate 

$ python3 manage.py runserver
```

Aplikacja DRF jest będzie dostępna na porcie 8000. To oczywiście sam backend więc nie wiem czy
będziesz chciał uruchamiać, instukcja na wszelki wypadek. Zawsze można coś potestować Postmanem albo curlem. 




   
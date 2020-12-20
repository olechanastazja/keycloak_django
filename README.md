## Keycloak + Django REST Framework

Library for DRF - Keycloak integration using OpenId Connect: 
https://github.com/ByteInternet/drf-oidc-auth
 
#### Installation

```
$ git clone https://github.com/olechanastazja/keycloak_django.git
$ cd keycloak_django
# docker-compose up
```

Keycloak should be ready to user on port 8080, example login and password for admin user are in docker-compose

Keycloak uses PostgreSQL database and DRF uses sqlite3 for now. 
The presented solution handles the situation when users are created in two databases. 
Users in database connected to Django endpoint are identified by email address that is the same as in keycloak
equivalent.

The DRF application in available on port 8000. It'a a backend application only. To check if it's working as expected
you can user Postman or curl.

##### Example requests

Create a user:
```
curl --location --request POST 'http://127.0.0.1:8000/example/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "john.doe@gmail.com",
    "username": "john",
    "first_name": "John",
    "last_name": "Doe",
    "keycloak_id": "9444faa2-16e5-4a4f-83ab-a1b3abe6b397"
}'
```
Get a user:
```
curl --location --request GET 'http://127.0.0.1:8000/example/users/john/'
```
Test secured endpoint:
```
curl --location --request GET 'http://127.0.0.1:8000/example/' \
--header 'Authorization: Bearer your_token'
```

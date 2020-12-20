FROM python:3.8.3

RUN mkdir /example_auth

RUN apt-get update

RUN apt-get install -y sqlite3 libsqlite3-dev

COPY . /example_auth/

RUN pip install -r /example_auth/requirements.txt

RUN chmod +x /example_auth/entrypoint.sh

ENTRYPOINT ["sh", "/example_auth/entrypoint.sh"]
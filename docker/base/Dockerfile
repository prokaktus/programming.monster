FROM python:3.8.2-alpine3.11

RUN mkdir /code
WORKDIR /code
RUN apk add libffi-dev musl-dev openssl-dev gcc
RUN pip install poetry

RUN apk add jpeg-dev zlib-dev postgresql-libs postgresql-dev

COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /code/

CMD ["uwsgi", "--ini", "uwsgi_docker.ini"]

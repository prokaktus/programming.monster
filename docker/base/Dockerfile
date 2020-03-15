FROM python:3.8.2-alpine3.11

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "--version"]

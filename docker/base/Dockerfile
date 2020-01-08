from python:3.7.4-alpine3.10

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "--version"]

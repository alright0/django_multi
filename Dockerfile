FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
WORKDIR /code/project/
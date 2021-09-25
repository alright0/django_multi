FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

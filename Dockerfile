FROM python:3.5

RUN apt-get update
RUN apt-get install postgresql-client -y

ARG uid=1000
ARG gid=1000
RUN addgroup --gid $gid workshop
RUN useradd -m --uid $uid -g workshop workshop


COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
ENV PYTHONPATH=/code
WORKDIR /code

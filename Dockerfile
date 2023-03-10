FROM python:3.10

RUN apt-get update
RUN apt-get install --no-install-recommends -y build-essential curl git nodejs npm

# Install the vendor applications
COPY ./vendor/dart-sass /var/dart-sass
ENV PATH="/var/dart-sass:${PATH}"

# install dependencies
RUN pip install --no-cache-dir --upgrade pip wheel
COPY ./requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

COPY ./gunicorn.conf.py /var/gunicorn.conf.py
COPY ./firebase.json /var/app/firebase.json


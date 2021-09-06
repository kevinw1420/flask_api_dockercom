FROM python:3.9.2

RUN mkdir -p /var/www/html/flask_api

WORKDIR /var/www/html/flask_api

ADD . /var/www/html/flask_api

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN chmod +x ./start.sh
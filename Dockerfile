FROM nginx:latest

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

RUN mkdir -p /var/app/src
COPY src /var/app/src
WORKDIR /var/app

COPY requirements.txt /var/app/requirements.txt

RUN apt-get update && \
    apt-get install -y python3 python3-pip libpq-dev && \
    pip3 install --upgrade pip && \
    pip3 install uwsgi && \
    pip3 install -r requirements.txt

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY uwsgi /var/app/uwsgi
COPY manage.py /var/app/manage.py
COPY startup.sh /var/app/startup.sh

CMD ["/bin/bash", "/var/app/startup.sh"]
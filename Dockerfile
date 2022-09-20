FROM python:3.8-slim-buster

COPY app.py /usr/bin/app.py
RUN true
COPY requirements.txt .
RUN true
RUN pip3 install -r requirements.txt

RUN true
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
FROM python:3.8-slim-buster

COPY app.py /app.py
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ADD app.py .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
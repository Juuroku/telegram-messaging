FROM python:3.8-slim-buster

COPY app.py /app.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

WORKDIR /github/workspace

ENTRYPOINT ["/entrypoint.sh"]
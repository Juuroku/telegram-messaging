FROM python:3.8-slim-buster

COPY app.py /app.py
RUN true
COPY requirements.txt .
RUN true
RUN pip3 install -r requirements.txt

ADD app.py .

RUN true
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh", "$INPUT_TELEGRAM-TOKEN", "$INPUT_TELEGRAM-CHAT", "$INPUT_MESSAGE", "$INPUT_PARSE"]
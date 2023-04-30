FROM python:3.8-slim-buster

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY consumer4.py consumer4.py

CMD ["python3", "consumer4.py"]


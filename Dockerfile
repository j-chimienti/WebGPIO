FROM python:3.5
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
COPY . .
RUN python backend.py

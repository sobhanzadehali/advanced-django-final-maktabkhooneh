FROM python:3.10.0-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY ./core /app/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
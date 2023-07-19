FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
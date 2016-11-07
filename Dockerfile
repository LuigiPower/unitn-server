FROM python:3
MAINTAINER emavgl

RUN apt-get update && apt-get install -y libmysqlclient-dev mysql-client

ENV FLASK_APP=runserver.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

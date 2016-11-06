FROM python:3-onbuild
MAINTAINER emavgl

RUN apt-get update && apt-get install -y libmysqlclient-dev mysql-client python3-mysqldb

ENV FLASK_APP=runserver.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

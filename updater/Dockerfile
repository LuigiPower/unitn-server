FROM python:3-onbuild
MAINTAINER emavgl

RUN apt-get update && apt-get install -y cron libmysqlclient-dev mysql-client python3-mysqldb
COPY crontab /etc/cron.d/updater
RUN chmod 0744 /etc/cron.d/updater && touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log

FROM python:3
MAINTAINER emavgl

RUN apt-get update && apt-get install -y cron libmysqlclient-dev mysql-client

# Create app folder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy requirements only and do pip install
# Good to do it here, so that when requirements stays the same, we don't run pip again
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /usr/src/app

COPY crontab /etc/cron.d/updater
RUN chmod 0744 /etc/cron.d/updater && touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
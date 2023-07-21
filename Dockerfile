FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3 python3-pip cron git -y

COPY files/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install requests

COPY infosec_mastodon.py /opt/infosec_mastodon.py
COPY files/update_infosec_csv.sh /opt/update_infosec_csv.sh
COPY files/docker_ssh_key /root/.ssh/id_rsa
COPY files/known_hosts /root/.ssh/known_hosts
RUN chmod 0400 /root/.ssh/id_rsa

RUN cd /opt/ && git clone git@github.com:cstromblad/infosec_mastodon.git
RUN git config --global user.email "github@x90.se"
RUN git config --global user.name "Christoffer Strömblad"

RUN crontab /etc/cron.d/crontab

ENTRYPOINT ["cron", "-f"]
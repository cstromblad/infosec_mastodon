FROM alpine:latest

# Getting the necessary stuff setup and installed.
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache python3
RUN python3 -m ensurepip
RUN apk add --no-cache git openssh

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

# Making crontab aware of the crontab...
RUN crontab /etc/cron.d/crontab

# ... and DONE. Let's get this party started!
ENTRYPOINT ["/usr/sbin/crond", "-f"]

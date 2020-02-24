FROM    python:3.7-slim

RUN     apt -y update && apt -y upgrade && apt -y autoremove
RUN     apt-get install vim -y
RUN     apt -y install nginx

# 도커 컨테이너 내부 /root/ 에 .aws 폴더 생성
RUN     mkdir /root/.aws
# requirements.txt 를 도커 컨테이너 내부에 넣음
COPY    ./requirements.txt /tmp/

RUN     pip install -r /tmp/requirements.txt

# docker container 의 /srv/에 Fest-Crawling 복사
COPY    . /srv/Festa-crawling

#RUN     rm /etc/nginx/sites-enabled/default
#RUN     cp /srv/Festa-crawling/.config/festa.nginx /etc/nginx/sites-enabled/

CMD     /bin/bash
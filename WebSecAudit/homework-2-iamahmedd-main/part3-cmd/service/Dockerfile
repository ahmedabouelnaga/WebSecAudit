FROM python:latest

COPY src /app

WORKDIR /app

RUN pip3 install -r /app/requirements.txt

RUN apt-get update && apt-get install -y iputils-ping

#RUN chmod +t /tmp/

#RUN export uid=1000 gid=1000 && \
#    echo "appuser:x:${uid}:${gid}:AppUser,,,:/app:/bin/bash" >> /etc/passwd && \
#    echo "appuser:x:${uid}:" >> /etc/group 

#USER appuser

CMD python3 run.py

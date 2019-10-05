FROM ubuntu:18.04

RUN apt-get update -y

RUN apt-get install -y python3.5
RUN apt-get install -y python3-pip

RUN pip3 install google-cloud-monitoring==0.33.0

ADD . /app

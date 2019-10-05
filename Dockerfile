FROM ubuntu:18.04

RUN apt-get update -y

RUN apt-get install -y python3.5
RUN apt-get install -y python3-pip

RUN pip3 install google-cloud-monitoring==0.33.0

ADD . /app

# Install gcloud
RUN apt-get install -y curl

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | \
	tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

RUN apt-get install -y apt-transport-https
RUN apt-get install -y ca-certificates

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
	apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

RUN apt-get update -y
RUN apt-get install -y google-cloud-sdk

# Install kubectl
RUN apt-get install -y kubectl

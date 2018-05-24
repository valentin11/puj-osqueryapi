FROM ubuntu:latest
MAINTAINER Valentin y Javier <valentinfer@javerianacali.edu.co>
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
################################################################################
# OsQuery Installation
################################################################################
RUN apt-get -y install software-properties-common
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1484120AC4E9F8A1A577AEEE97A80C63C9D8B80B
RUN add-apt-repository "deb [arch=amd64] https://osquery-packages.s3.amazonaws.com/xenial xenial main"
RUN apt-get update
RUN apt-get install osquery
################################################################################
# Install requirements: git, jq, python
################################################################################
RUN apt-get update && apt-get -y install vim git jq curl sudo wget python python-pip
RUN pip install --upgrade pip
################################################################################
# Install osquery and python bindings
################################################################################
RUN wget https://pkg.osquery.io/linux/osquery-3.2.4_1.linux_x86_64.tar.gz
RUN tar xzvf osquery-3.2.4_1.linux_x86_64.tar.gz
RUN pip install osquery
RUN mkdir /home/workdir
RUN git clone https://github.com/osquery/osquery-python.git

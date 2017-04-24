FROM ubuntu:16.10
MAINTAINER jacobrepp@gmail.com

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y bzip2 telnet net-tools

#ADD https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh .
ADD Anaconda3-4.3.1-Linux-x86_64.sh .
RUN /bin/bash Anaconda3-4.3.1-Linux-x86_64.sh -b -f -p /anaconda3

# Cleanup the installer
RUN rm -f Anaconda3-4.3.1-Linux-x86_64.sh 

EXPOSE 8888

RUN mkdir /notebooks
ADD jupyter_notebook_config.py .
ADD start_notebook.sh .

ENTRYPOINT ["/start_notebook.sh"]

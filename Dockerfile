FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -r requirements.txt
RUN mkdir /Adv-Auto-Filter-Bot-V2
WORKDIR /Adv-Auto-Filter-Bot-V2
RUN python3 -m bot

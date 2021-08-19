FROM python:3.9.5-slim-buster
WORKDIR /app
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "bot"]

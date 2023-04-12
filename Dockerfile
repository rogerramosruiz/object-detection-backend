FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-tk -y
RUN apt-get install python3-opencv -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/ .

CMD ["python3", "main.py"]
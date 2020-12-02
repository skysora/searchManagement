FROM python:3.7

COPY . /
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN \
apt-get update -y && \
apt-get install python3-pip -y && \
pip3 install bs4 && \
pip3 install numpy && \
pip3 install pymysql && \
pip3 install requests && \
apt-get install python3-lxml -y && \
pip3 install Pillow && \
apt-get install libopenjp2-7 -y && \
apt-get install libtiff5 -y && \
pip3 install Django

CMD [ "python3" ]

FROM alpine:3.7
MAINTAINER Simone Zabberoni <simone.zabberoni@gmail.com>

RUN apk add --update python3 py-pip
RUN pip install pyowm

ADD . /pyowm
WORKDIR /pyowm
ENTRYPOINT ["/pyowm/owm-cli.py"]


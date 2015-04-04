FROM dockerfile/ubuntu

RUN \
  sudo apt-get update && \
  sudo apt-get -y install build-essential && \
  sudo apt-get -y install libssl-dev libffi-dev && \
  sudo apt-get -y install python-dev python3-pip && \ 
  sudo pip3 install twisted && \
  sudo pip3 install autobahn && \
  sudo pip3 install pyopenssl && \
  sudo pip3 install python-chess && \
  sudo pip3 install pillow

RUN mkdir /slackChess/
COPY config.json /slackChess/
COPY main.py /slackChess/
COPY slackRequests.py /slackChess/
RUN mkdir /slackChess/game/
COPY game/ /slackChess/game/

RUN mkdir /resources/
RUN mkdir /resources/images/
RUN mkdir /resources/boards/
COPY resources/ /resources/images/

ENV SLACKBOT="asdjasd" 
ENV SLACKAPI="ASDJASD"

EXPOSE 80
CMD ["python3", "/slackChess/main.py"]

FROM ubuntu:16.04
# install boot
RUN apt-get update && apt-get clean && apt-get install -y \
    software-properties-common \
    x11vnc \
    xvfb \
    fluxbox \
    wmctrl \
    wget \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get -y install google-chrome-stable
RUN add-apt-repository universe

RUN useradd apps \
    && mkdir -p /home/apps \
    && chown -v -R apps:apps /home/apps
RUN apt-get update && apt-get clean && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install pyautogui

COPY bootstrap.sh /

CMD '/bootstrap.sh'

FROM mooghen/ch:June-15-17
RUN apt-get install -y \
  scrot \
  python3-tk \
  python3-dev \
  && pip3 install pyautogui

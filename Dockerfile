FROM mooghen/ch:June-15-17
RUN apt-get install -y \
  scrot \
  python3-tk \
  python3-dev \
  && python3 -m pip install pyautogui

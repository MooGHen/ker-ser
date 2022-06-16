set mus=%random%%random%%random%%random%
echo %mus%
start "" chrome.exe --profile-directory="%mus%" https://chrome.google.com/webstore/detail/youtube-ad-auto-skipper/lokpenepehfdekijkebhpnpcjjpngpnd
python test.py
start "" chrome.exe --profile-directory="%mus%" https://youtu.be/ZLEekcq1PTg
python startvideo.py

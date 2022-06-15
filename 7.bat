start "" chrome.exe --profile-directory="%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%" --app="data:text/html,<html><body><script>window.moveTo(800,640);window.resizeTo(300,200);window.location='https://youtu.be/-2ajSaGXf0Q';</script></body></html>" --proxy-server="127.0.0.1:%RANDOM%"
ping 127.0.0.1 -n 2
set /a num=%random% %%30 +50
set loopcount=%num%
:loop
ping 127.0.0.1 -n 2
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
exit 0

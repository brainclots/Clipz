@echo off
pushd %GDRIVE%\Music\Soundz

echo| set /p="The current log on sound is set to : "
type logon.txt
echo| set /p="The current log off sound is set to : "
type logoff.txt

:opt
echo.
choice /c 12rq /m "Press 1 to hear logon sound, 2 to hear logoff sound, r to reset sounds, q  to quit. "

if ERRORLEVEL 4 goto :audi9000
if ERRORLEVEL 3 call .\LogOff\SetNextLogonLogoffSound.bat
if ERRORLEVEL 2 echo | set /p="Playing " & type logoff.txt & swavplayer "%GDRIVE%\Music\Soundz\currentlogoff.wav"
if ERRORLEVEL 1 echo | set /p="Playing " & type logon.txt & swavplayer "%GDRIVE%\Music\Soundz\currentlogon.wav"
goto :opt

:audi9000
popd
exit /b

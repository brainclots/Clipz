@echo off & setlocal EnableDelayedExpansion
pushd %GDRIVE%\Music\Soundz

:opt
set /p LOGON=<logon.txt
set /p LOGOFF=<logoff.txt
echo.
set message=Press [N] to play the logon sound: !LOGON!^

Press [F] to play the logoff sound: !LOGOFF!^

Press [R] to pick new sounds^

Press [Q] to quit.
echo !message!
choice /c nfrq
set SELECTION=%ERRORLEVEL%

if %SELECTION% EQU 1 echo | set /p="The logon sound is set to !LOGON!"  & swavplayer "%GDRIVE%\Music\Soundz\currentlogon.wav"
if %SELECTION% EQU 2 echo | set /p="The logoff sound is set to !LOGOFF!" & swavplayer "%GDRIVE%\Music\Soundz\currentlogoff.wav"
if %SELECTION% EQU 3 call .\LogOff\SetNextLogonLogoffSound.bat
if %SELECTION% EQU 4 goto :audi9000
goto :opt

:audi9000
popd
exit /b

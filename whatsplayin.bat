@echo off & setlocal EnableDelayedExpansion
pushd %GDRIVE%\Music\Soundz

:opt
set /p LOGON=<logon.txt
set /p LOGOFF=<logoff.txt
echo.
set message=Press [1] to play the logon sound: !LOGON!^

Press [2] to play the logoff sound: !LOGOFF!^

Press [R] to pick new sounds^

Press [Q] to quit.
echo !message!
choice /c 12rq
set SELECTION=%ERRORLEVEL%

if %SELECTION% EQU 1 echo | set /p="The logon sound is set to !LOGON!"  & swavplayer "%GDRIVE%\Music\Soundz\currentlogon.wav"
if %SELECTION% EQU 2 echo | set /p="The logoff sound is set to !LOGOFF!" & swavplayer "%GDRIVE%\Music\Soundz\currentlogoff.wav"
if %SELECTION% EQU 3 goto :RESET
if %SELECTION% EQU 4 goto :audi9000
goto :opt

:RESET
set oncount=0
set offcount=0

for /f "tokens=*" %%i in ('dir /b "%GDRIVE%\Music\Soundz\Logon\*.wav"') DO (
  set /a oncount+=1
)
for /f "tokens=*" %%j in ('dir /b "%GDRIVE%\Music\Soundz\Logoff\*.wav"') DO (
  set /a offcount+=1
)

echo.
echo There are !oncount! logon sound files available, and !offcount! logoff sounds available. The lucky ones are:
call .\LogOff\SetNextLogonLogoffSound.bat
goto :opt

:audi9000
popd
exit /b

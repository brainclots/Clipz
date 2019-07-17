@echo off & setlocal EnableDelayedExpansion
pushd %GDRIVE%\Music\Soundz

:opt
set /p LOGON=<logon.txt
set /p LOGOFF=<logoff.txt
echo.
set oncount=0
set offcount=0

for /f "tokens=*" %%i in ('dir /b "%GDRIVE%\Music\Soundz\Logon\*.wav"') DO (
  set /a oncount+=1
)
for /f "tokens=*" %%j in ('dir /b "%GDRIVE%\Music\Soundz\Logoff\*.wav"') DO (
  set /a offcount+=1
)

echo There are currently !oncount! logon sounds, and the one queued is !LOGON!
voice /female There are currently !oncount! logon sounds, and the one queued is !LOGON!
swavplayer "%GDRIVE%\Music\Soundz\currentlogon.wav"

echo There are currently !offcount! logoff sounds, and the one queued is !LOGOFF!
voice /female And there are !offcount! logoff sounds, and the one queued is !LOGOFF!
swavplayer "%GDRIVE%\Music\Soundz\currentlogoff.wav"

:RESET
choice /m "Pick new sounds?"
set SELECTION=%ERRORLEVEL%

IF %SELECTION% EQU 1 call .\LogOff\SetNextLogonLogoffSound.bat -v

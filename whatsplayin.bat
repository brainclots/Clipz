@echo off
pushd %GDRIVE%\Music\Soundz

echo| set /p="The current log on sound is set to : "
type logon.txt
echo| set /p="The current log off sound is set to : "
type logoff.txt

:opt
echo.
choice /c nfrq /m "Press [N] to hear logon sound, [F] to hear logoff sound, [R] to reset sounds, [Q] to quit. "
set SELECTION=%ERRORLEVEL%

if %SELECTION% EQU 1 echo | set /p="The logon sound is set to " & type logon.txt & swavplayer "%GDRIVE%\Music\Soundz\currentlogon.wav"
if %SELECTION% EQU 2 echo | set /p="The logoff sound is set to " & type logoff.txt & swavplayer "%GDRIVE%\Music\Soundz\currentlogoff.wav"
if %SELECTION% EQU 3 call .\LogOff\SetNextLogonLogoffSound.bat
if %SELECTION% EQU 4 goto :audi9000
goto :opt

:audi9000
popd
exit /b

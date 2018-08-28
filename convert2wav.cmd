@echo off

set CMD_DIR=%USERPROFILE%\Downloads\ffmpeg-win-2.2.2
set CONVERTERAPP=ffmpeg.exe

if "%1" EQU "" echo Usage: %0 ^<mp3_filename^> ^<desired_wav_filename^> & exit /b

%CMD_DIR%\%CONVERTERAPP% -i %1 %2 2> nul
echo | set /p="%1 "
echo was converted to %2

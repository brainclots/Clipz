@echo off

set CMD_DIR=%USERPROFILE%\Downloads\ffmpeg-win-2.2.2
set CONVERTERAPP=ffmpeg.exe
set MP3="%1"
set CURRENT_DIR=%~dp1
set BASENAME=%~n1

set DEST_WAV=%~nx2
if not defined DEST_WAV set DEST_WAV=%BASENAME%.wav

set DEST_DIR=%~dp2
if not defined DEST_DIR set DEST_DIR=.

if "%1" == "" echo Usage: %0 ^<mp3_filename^> [^<desired_wav_filename^>] & exit /b

%CMD_DIR%\%CONVERTERAPP% -y -i %MP3% "%DEST_DIR%\%DEST_WAV%" 2> nul

echo | set /p=%MP3%
echo. was converted to %DEST_DIR%\%DEST_WAV%

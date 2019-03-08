@echo off & setLocal EnableDelayedExpansion

:: Go to the Clipz directory
pushd "%CLIPZ%"

:: Initialize counters
set mp3count=0
set wavcount=0

:: Get a Carriage Return (Ascii 13) in CR variable:
for /F %%a in ('copy /Z "%~F0" NUL') do set "CR=%%a"

:: Count files
start /b swavplayer "%GDRIVE%\Music\Soundz\Effects\yaheyahe2.wav"

for /f "tokens=*" %%f in ('dir /b *.wav *.mp3 ^| sort') DO (
	if "%%~xf"==".wav" (set /a wavcount+=1)
	if "%%~xf"==".mp3" (set /a mp3count+=1)
	< NUL set /p "=Counting !wavcount! wav files and !mp3count! mp3 files. !CR!"
	set excused="no"
	:: See if the file is in the list of excused files
	if NOT EXIST %%f.txt (
		for /f %%i in (no_words.txt) DO (
			if %%f EQU %%i set excused="yes"
		)
	if !excused! EQU "no" set UNEXCUSED=!UNEXCUSED!,%%f
	)
)
call :parse "%UNEXCUSED%"
goto :end

:parse
setlocal
set list=%1
set list=%list:"=%
for /f "tokens=1* delims=," %%n in ("%list%") DO (
	if not "%%n" == "" call :tellit "%%n"
	if not "%%o" == "" call :parse "%%o"
)
endlocal
exit /b

:tellit
setlocal
echo %1 does not have a word file.
endlocal
exit /b

:end
:: Get & display totalcount
set /a totalcount=%wavcount% + %mp3count%
echo.
echo.  WAV files: %wavcount%
echo.  MP3 files: %mp3count%
echo Total clips: %totalcount%
start /b swavplayer "%GDRIVE%\Music\Soundz\Effects\fanfare1.mp3"

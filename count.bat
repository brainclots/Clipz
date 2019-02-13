@echo off & setLocal EnableDelayedExpansion

:: Go to the Clipz directory
pushd "%CLIPZ%"

:: Initialize counters
set mp3count=0
set wavcount=0

:: Count files
start /b swavplayer "%GDRIVE%\Music\Soundz\Effects\hanbar02.wav"
for /f "tokens=*" %%f in ('dir /b *.wav *.mp3') DO (
	if "%%~xf"==".wav" (set /a wavcount+=1)
	if "%%~xf"==".mp3" (set /a mp3count+=1)

	set excused="no"
	:: See if the file is in the list of excused files
	if NOT EXIST %%f.txt (
		for /f %%i in (no_words.txt) DO (
			if %%f EQU %%i set excused="yes"
		)
	if !excused! EQU "no" echo %%f does not have a wordfile
	)
	cls
	echo.
	echo.  Counting...
	echo.  WAV files: !wavcount!
	echo.  MP3 files: !mp3count!
)

:: Get & display totalcount
set /a totalcount=%wavcount% + %mp3count%
echo.  Total clips: %totalcount%
start /b swavplayer "%GDRIVE%\Music\Soundz\Effects\fanfare1.mp3"

@echo off & setLocal EnableDelayedExpansion

:: Go to the Clipz directory
pushd "%CLIPZ%"

:: Initialize counters
set mp3count=0
set wavcount=0

:: Count wav files
for /f "tokens=*" %%f in ('dir /b *.wav') DO (
	set /a wavcount+=1
)
echo WAV files: %wavcount%

:: Count MP3 files
for /f "tokens=*" %%f in ('dir /b *.mp3') DO (
	set /a mp3count+=1
)
echo MP3 files: %mp3count%

:: Get & display total
set /a totalcount=%wavcount% + %mp3count%
echo Total clips: %totalcount%

:: Check whether each file is excused from having corresponding txt file
for /f "tokens=*" %%f in ('dir /b *.wav *.mp3') DO (
	set excused="no"
	:: See if the file is in the list of excused files
	if NOT EXIST %%f.txt (
		for /f %%i in (no_words.txt) DO (
			if %%f EQU %%i set excused="yes"
		)

	if !excused! EQU "no" echo %%f does not have a wordfile
	)
)

@echo off & setLocal EnableDelayedExpansion

pushd "%CLIPZ%"

set mp3count=0
set wavcount=0
for /f "tokens=*" %%f in ('dir /b *.wav') DO (
	set /a wavcount+=1
)
echo WAV files: %wavcount%

for /f "tokens=*" %%f in ('dir /b *.mp3') DO (
	set /a mp3count+=1
)
echo MP3 files: %mp3count%

set /a totalcount=%wavcount% + %mp3count%
echo Total clips: %totalcount% 

for /f "tokens=*" %%f in ('dir /b *.wav *.mp3') DO (
	set excused="no"
	if NOT EXIST %%f.txt (
		for /f %%i in (no_words.txt) DO (
			if %%f EQU %%i set excused="yes"
		)

	if !excused! EQU "no" echo %%f does not have a wordfile
	)
)

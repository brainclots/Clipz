@echo off & setLocal EnableDelayedExpansion

:: Make list of wav and mp3 files in directory
pushd "%GDRIVE%\Music\Soundz\Clipz"

:: Loop through list, numbering each file in an array
set n=0
for /f "tokens=*" %%f in ('dir /b *.mp3 *.wav') DO (
	set /A n = !n! + 1
	set "clip[!n!]=%%f"
)

:playit

:: Pick a random number between 1 and the number of files
set /a randomclip=(%random% %% !n!) + 1
set filename=!clip[%randomclip%]!
set soundfile=%filename%

:: Set title bar to name of the file
title Playing %filename%

:: Find the matching file with text of the clip
if EXIST "%filename%.txt" (
	set "words=%filename%.txt"
) ELSE (
	set "words=snarky.txt"
)

:: Count how many lines are in the file with text
set lines=0
for /f usebackq %%a in ("%words%") DO (set /a lines+=1)

:: Set the size of the window to match length of file + lines for snark shark!
set /a lines=%lines%+44
color 3f
mode con: cols=70 lines=%lines%

:: Display top of speech bubble
echo.
echo. __________________
echo /                  \

:: Display text and shark
type "%words%"
type snarkshark.txt

::Display filename centered under shark
:centerloop
IF "%filename:~17,1%" neq "" GOTO showname
SET "filename=%filename% "
IF "%filename:~17,1%" neq "" GOTO showname
SET "filename= %filename%"
GOTO centerloop
:showname
echo                          ( %filename% )

:: Play sound
swavplayer "%soundfile%" > nul

:: Set random wait time of 15 to 120 seconds
set /a timeleft=(%random% %% 105) + 15

:countdownloop
color 20
mode con: cols=55 lines=22
for %%i in (0,1,2,3,4,3,2,1) do (
  if !timeleft! EQU 0 goto :playit
  cls
  echo.
  type eightball%%i.txt
  echo.
  echo             Sleeping for !timeleft! seconds...
  echo                        Zzzzzzzz....
  echo.
  choice /c NPQW /m "~~~    Press N for next, P for pause, Q to quit    ~~~" /N /t 1 /d W

set SELECTION=!ERRORLEVEL!
if !SELECTION! EQU 1 goto :playit
if !SELECTION! EQU 2 pause && set timeleft=1
if !SELECTION! EQU 3 goto :leaveloop

set /a timeleft-=1
)
if !timeleft! GTR 0 goto :countdownloop

goto :playit

:leaveloop
:: Clean up
color
cls
mode con: cols=120 lines=30
title %comspec%

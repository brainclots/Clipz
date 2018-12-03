@echo off & setLocal EnableDelayedExpansion

:playit
call "%GDRIVE%\Music\Soundz\Clipz\eightball.bat"
title ~~~ Shaking the Eightball ~~~
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
  if !SELECTION! EQU 2 goto :chill
  if !SELECTION! EQU 3 goto :leaveloop
  set /a timeleft-=1
)
if %timeleft% GTR 0 goto :countdownloop

goto :playit

:chill
cls
echo.
echo.
echo.
echo                    --=== PAUSED ===--
echo.
echo.
pause
::set timeleft=1
goto :playit

:leaveloop
cls
color 07
mode con: cols=120 lines=30
title %comspec%

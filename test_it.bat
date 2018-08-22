@echo off
SETLOCAL EnableDelayedExpansion

if "%1" EQU "" echo Test what? && exit /b
set DIR=%~dp1
pushd %DIR%
set filename=%~nx1
if not exist %filename% echo %1 not found! && exit /b
if exist %filename%.txt (
  set wordfile=%filename%.txt
) else (
  set wordfile="%CLIPZ%\snarky.txt"
)
cls

:: Count how many lines are in the file with text
set lines=0
for /f usebackq %%a in (%wordfile%) DO (set /a lines+=1)

:: Set the size of the window to match length of file + lines for snark shark!
set /a lines=%lines%+30
mode con: cols=120 lines=%lines%

echo.
echo  __________________
echo /                  \
type %wordfile%
type "%CLIPZ%\snarkshark_short.txt"

:showname
echo                                                           (%filename%)
title Playing %filename%
swavplayer "%DIR%\%filename%" > nul
::mode con: cols=100 lines=25

title %comspec%

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

if "%2" NEQ "" (
  set image=%2
  if not exist "!image!" echo No such image file "!image!" && exit /b
) else (
  set image="%CLIPZ%\snarkshark_short_img.txt"
)
cls
:: Count how many lines are in the image file
set img_lines=0
for /f usebackq %%a in (%image%) DO (set /a img_lines+=1)
:: Count how many lines are in the file with text
set txt_lines=0
for /f usebackq %%a in (%wordfile%) DO (set /a txt_lines+=1)

:: Set the size of the window to match length of file + lines for image
set /a lines=%txt_lines%+%img_lines%+10
mode con: cols=120 lines=%lines%
color F0

echo.
echo  __________________
echo /                  \
type %wordfile%
type %image%

:showname
echo                                                                               ( %filename% )
title Playing %filename%
swavplayer "%DIR%\%filename%" > nul
::mode con: cols=100 lines=25
color 07
title %comspec%

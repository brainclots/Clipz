:: Add a new file to the list of files being sourced by the eightball.py script
@echo off

if "%1" EQU "" (
  echo ERROR: What file are we adding?
  goto eof
)

set FILE2ADD=%1

if not EXIST %FILE2ADD% (
  echo ERROR: File %FILE2ADD% does not exist!
  goto eof
)

echo %cd%\%FILE2ADD% >> listofiles.txt
echo.
echo Successfully added %cd%\%FILE2ADD% to listofiles.txt
echo.

:eof

@echo off

if "%1"=="" echo Bring what? && exit /b 1
if EXIST %1 start /wait audacity %1
if EXIST \cleaned\%1 move \cleaned\%1 .

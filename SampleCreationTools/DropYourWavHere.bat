@echo off
cd /D "%~dp0"

:Loop

z64audio.exe --i %1 --I 50 --o %~n1.bin

REM Rename output config.toml to unique name matching wav input file
ren config.toml "%~n1.toml"
ren "%~n1.book.bin" "%~n1.book"
ren "%~n1.loopbook.bin" "%~n1.loopbook"

REM // Move all files to output subfolder
if not exist output\ md output

move "%~n1.toml" output
move "%~n1.vadpcm.bin" output


REM // Handle multiple arguments
SHIFT
IF "%~1" NEQ "" (GOTO Loop)

pause

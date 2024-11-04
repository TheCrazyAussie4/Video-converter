@echo off
setlocal enabledelayedexpansion

REM Use the provided input file and output path
set "INPUT_FILE=C:/Users/thecr/Desktop/28-01 11-01-11.mkv"
set "OUTPUT_PATH=C:/Users/thecr/Desktop/Converter/output"

REM Extract the name of the input file without extension
for %%f in ("%INPUT_FILE%") do set "name=%%~nf"

set "outname=%OUTPUT_PATH%\%name%"
echo Converting: %INPUT_FILE% to %outname%.mp4

REM Run ffmpeg to convert while keeping resolution, framerate, and setting very high quality
ffmpeg -i "%INPUT_FILE%" -c:v h264_nvenc -crf 16 -preset slow -c:a aac -b:a 256k -movflags +faststart "%outname%.mp4"

pause

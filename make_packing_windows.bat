@echo off
setlocal

REM Change directory to the script's location (assumed to be the root directory)
cd /d %~dp0

REM Check if build or dist directories exist
if exist build (
    set DIR_FOUND=1
)
if exist dist (
    set DIR_FOUND=1
)

REM If either build or dist exists, prompt the user once
if defined DIR_FOUND (
    echo Warning build or dist directory found
    set /p CONTINUE=Do you want to proceed and delete them? (Y/N)     

    REM If user inputs N, exit the script
    if /I "%CONTINUE%"=="N" (
        echo Operation aborted by user
        exit /b
    )

    REM If user inputs Y, delete the directories and proceed
    if /I "%CONTINUE%"=="Y" (
        echo Deleting build and dist directories...
        if exist build rmdir /s /q build
        if exist dist rmdir /s /q dist
        echo Directories deleted
    ) else (
        echo Invalid input. Operation aborted.
        exit /b
    )
)

REM Run PyInstaller to build the project
echo Running PyInstaller...
pyinstaller installer_packing.spec

echo Build completed!
pause

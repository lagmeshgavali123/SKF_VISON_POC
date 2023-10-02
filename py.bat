@echo off
setlocal enabledelayedexpansion

REM Specify the Python version and download URL
set PYTHON_VERSION=3.10.2
set DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

REM Set the installation directory
set INSTALL_DIR=C:\Python\Python%PYTHON_VERSION%

REM Download Python installer
echo Downloading Python %PYTHON_VERSION%...
curl -o python-%PYTHON_VERSION%-amd64.exe %DOWNLOAD_URL%

REM Install Python
echo Installing Python %PYTHON_VERSION%...
python-%PYTHON_VERSION%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Verify the installation
for /f "tokens=*" %%i in ('where python') do set PYTHON_PATH=%%i
if exist !PYTHON_PATH! (
    echo Python %PYTHON_VERSION% has been installed successfully.
) else (
    echo Failed to install Python %PYTHON_VERSION%.
)

REM Clean up the installer
del python-%PYTHON_VERSION%-amd64.exe

REM Pause to allow viewing the output
pause

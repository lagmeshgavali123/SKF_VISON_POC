@echo off

REM Set the base path to the script's directory
set BASE_PATH=%~dp0

call cd image-capture_new
call python -m venv myenv


REM Create and activate the Python environment
call myenv\Scripts\activate
call python -m pip install django
call python -m pip install ultralytics
call python -m pip install psycopg2
call cd ..
REM Run postgres_setup.py and wait for it to complete
start cmd /c "python postgres_setup.py"
if %errorlevel% neq 0 (
    echo Error: postgres_setup.py failed.
    exit /b %errorlevel%
)

REM Navigate to the Django project folder
cd /d "%BASE_PATH%\image-capture_new"

REM Start manage.py runserver in the background
start cmd /c "python manage.py runserver"

REM Wait for a few seconds (adjust as needed)
timeout /t 8
cd /d ..

REM Minimize the Command Prompt window
powershell -windowstyle hidden -command "(New-Object -ComObject Shell.Application).ToggleDesktop()"

REM Run UI.py (this will be executed after you manually close the manage.py runserver)
python UI.py

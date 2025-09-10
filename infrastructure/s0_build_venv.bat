@echo off
setlocal enabledelayedexpansion
::----------------------------------------------------------------------------------------------------------------------
SET "PATH_VENV=%~dp0venv\p310_lab_01_win"
SET "REQ_FILE=%~dp0requirements.txt"
SET "PATH_PYTHON=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
::----------------------------------------------------------------------------------------------------------------------
IF NOT EXIST "%PATH_PYTHON%" (
  ECHO [ERROR] Python not found at "%PATH_PYTHON%"
  exit /b 1
)
::----------------------------------------------------------------------------------------------------------------------
IF NOT EXIST "%PATH_VENV%" (
  ECHO [INFO] Creating venv at "%PATH_VENV%"...
  "%PATH_PYTHON%" -m venv "%PATH_VENV%" || (ECHO [ERROR] venv create failed & exit /b 1)
)
::----------------------------------------------------------------------------------------------------------------------
CALL "%PATH_VENV%\Scripts\activate.bat"
"%PATH_VENV%\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel packaging
"%PATH_VENV%\Scripts\python.exe" -m pip install --prefer-binary -r "%REQ_FILE%"
::----------------------------------------------------------------------------------------------------------------------
ECHO -----------------------------------------------
ECHO Virtual environment setup complete at "%PATH_VENV%"
ECHO Activate it with:
ECHO %PATH_VENV%\Scripts\activate.bat
ECHO -----------------------------------------------
endlocal
exit /b 0

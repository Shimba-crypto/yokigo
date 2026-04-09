@echo off
title YOKIGO | SYSTEM DEPLOYMENT
color 0b

echo ========================================
echo       YOKIGO INSTALLER PROTOCOL        
echo ========================================
echo.

:: 1. CHECK FOR PYTHON
echo [*] Checking for Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] 'python' command not found. Checking for 'py' launcher...
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo [!!] No Python detected. Downloading installer...
        powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe' -OutFile 'python_installer.exe'"
        echo [*] Installing Python (Silent Mode)...
        start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
        del python_installer.exe
        echo [+] Python installation complete.
    ) else (
        echo [+] 'py' launcher detected.
    )
) else (
    echo [+] 'python' command detected.
)

:: 2. INSTALL LIBRARIES (Checking both commands)
echo [*] Syncing dependencies...
python -m pip install colorama psutil pyinstaller >nul 2>&1 || py -m pip install colorama psutil pyinstaller

:: 3. DOWNLOAD PROJECT
echo [*] Fetching Yokigo Project Files from GitHub...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/Shimba-crypto/yokigo/archive/refs/heads/main.zip' -OutFile 'yokigo.zip'"
powershell -Command "Expand-Archive -Path 'yokigo.zip' -DestinationPath '.' -Force"
del yokigo.zip

:: 4. THE SMART BUILDER (Fail-safe logic)
cd yokigo-main
echo [*] Initializing Packager...

:: Try python first
python packager.py
if %errorlevel% neq 0 (
    echo [!] 'python' build failed. Attempting with 'py' launcher...
    py packager.py
    if %errorlevel% neq 0 (
        echo [CRITICAL] Both 'python' and 'py' failed to run the packager.
        pause
        exit
    )
)

echo.
echo ========================================
echo    DEPLOYMENT COMPLETE: CHECK /DIST
echo ========================================
pause

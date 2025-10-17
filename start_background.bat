@echo off
title AI File Manager
echo 🤖 AI File Manager - Background Service
echo 📅 Started: %date% %time%
echo.

cd /d "D:\ai_file_manager"

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found in PATH
    echo 💡 Check Python installation
    pause
    exit /b 1
)

:: Check if required files exist
if not exist "start_manager.py" (
    echo ❌ start_manager.py not found
    pause
    exit /b 1
)

echo ✅ Starting AI File Manager service...
echo 📊 Monitoring all drives and folders
echo ⏹️  Service will run in background
echo 📝 Logs: ai_file_manager.log
echo.

:: Start the service (pythonw.exe runs without console window)
pythonw.exe start_manager.py --start

echo ❌ Service stopped or encountered an error
echo 🔄 It will restart on next login
timeout /t 5
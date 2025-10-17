@echo off
echo 🤖 Setting up AI File Manager Autostart...
echo.

:: Check admin privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Please run as Administrator
    echo 🔧 Right-click -> Run as administrator
    pause
    exit /b 1
)

:: Create task to run your start_background.bat on login
schtasks /create /tn "AIFileManager" /tr "D:\ai_file_manager\start_background.bat" /sc onlogon /ru System /f

echo ✅ Autostart configured successfully!
echo.
echo 📋 Task Details:
echo • Name: AIFileManager
echo • Trigger: On user logon
echo • Action: Runs start_background.bat
echo.
echo 🛠️ Management commands:
echo • Check task: schtasks /query /tn AIFileManager
echo • Delete task: schtasks /delete /tn AIFileManager /f
echo • Test now: schtasks /run /tn AIFileManager
echo.
pause
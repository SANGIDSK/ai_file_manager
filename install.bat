@echo off
echo 🤖 Setting up AI File Manager Automation...

mkdir ai_file_manager 2>nul
cd ai_file_manager

echo 📦 Installing dependencies...
python -m pip install schedule watchdog psutil

echo 🚀 Starting automation service...
python start_manager.py --start

echo ✅ AI File Manager is now running!
echo 📊 Check logs: type ai_file_manager.log
pause

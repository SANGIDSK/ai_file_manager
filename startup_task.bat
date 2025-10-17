@echo off
echo 📅 Adding AI File Manager to Windows startup...
schtasks /create /tn "AIFileManager" /tr "D:\ai_file_manager\start_background.bat" /sc onlogon /ru System
echo ✅ AI File Manager will now start automatically with Windows

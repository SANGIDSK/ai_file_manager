# check_admin.py
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("✅ Running as Administrator")
    print("🎯 AI Manager has full system access")
else:
    print("❌ Running as standard user")
    print("💡 Some features may be limited")

# Check what we can access
import psutil
print(f"📊 Can monitor system: {True}")  # psutil works regardless
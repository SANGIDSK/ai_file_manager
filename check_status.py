# check_status.py
import psutil
import time
from datetime import datetime

def check_ai_manager():
    print("🔍 Checking AI File Manager status...")
    
    # Check if Python processes are running
    python_processes = []
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if 'python' in proc.info['name'].lower():
                cmdline = proc.info['cmdline'] or []
                if any('start_manager.py' in str(cmd) for cmd in cmdline):
                    python_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    if python_processes:
        print(f"✅ AI File Manager is RUNNING ({len(python_processes)} processes)")
        for proc in python_processes:
            print(f"   Process ID: {proc.pid}, Running since: {datetime.fromtimestamp(proc.create_time())}")
    else:
        print("❌ AI File Manager is NOT running")
        print("💡 Start it with: python start_manager.py --start")
    
    # Show next scheduled tasks
    print("\n📅 Next scheduled tasks:")
    from datetime import datetime, timedelta
    now = datetime.now()
    print(f"   Organization: Every 2 hours (next: {(now + timedelta(hours=2)).strftime('%H:%M')})")
    print(f"   Backup: Daily at 01:00 AM")
    print(f"   Cleanup: Daily at 02:00 AM")

if __name__ == "__main__":
    check_ai_manager()

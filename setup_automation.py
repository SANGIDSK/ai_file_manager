import os
import subprocess
import sys
from pathlib import Path

def setup_automation():
    print("🔧 Setting up AI File Manager Automation...")
    
    # Create directories
    Path('logs').mkdir(exist_ok=True)
    Path('backups').mkdir(exist_ok=True)
    
    # Install packages
    requirements = ['schedule', 'watchdog', 'psutil']
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ Installed {package}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Could not install {package}")
    
    # Create startup configuration
    config = {
        "backup_location": str(Path.home() / "Backups"),
        "monitored_folders": [
            str(Path.home() / "Downloads"),
            str(Path.home() / "Desktop")
        ]
    }
    
    import json
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Setup complete!")
    print("\n🚀 Start with: python start_manager.py --start")

if __name__ == "__main__":
    setup_automation()

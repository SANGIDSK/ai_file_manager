# start_manager.py
import argparse
import sys
from pathlib import Path

# Add current directory to Python path
sys.path.append(str(Path(__file__).parent))

try:
    from automation_controller import AutomationController
    from auto_organizer import AutoOrganizer
    from disk_cleaner import DiskCleaner
    from backup_manager import BackupManager
    from config import config
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📝 Some components missing, using fallback mode")
    # We'll use dummy classes if real ones aren't available

def main():
    parser = argparse.ArgumentParser(description='AI File Manager - Multi-Drive')
    parser.add_argument('--start', action='store_true', help='Start automation service')
    parser.add_argument('--run', choices=['organize', 'cleanup', 'backup'], help='Run a specific task immediately')
    parser.add_argument('--show-drives', action='store_true', help='Show monitored drives and folders')
    
    args = parser.parse_args()
    
    if args.show_drives:
        try:
            print("🚀 AI File Manager - Multi-Drive Monitoring")
            print("=" * 50)
            print("📀 Monitored Drives:")
            for drive in config.monitored_drives:
                print(f"   • {drive}")
            print("\n📁 System Folders:")
            for folder in config.monitored_folders:
                print(f"   • {folder}")
            print("\n🎯 Custom Folders:")
            for folder in config.custom_folders:
                print(f"   • {folder}")
            print("\n🚫 Excluded Folders:")
            for folder in config.excluded_folders:
                print(f"   • {folder} (IGNORED)")
            print(f"\n🎯 Total ACTIVE monitored locations: {len(config.get_all_monitored_paths())}")
        except:
            print("📀 Monitoring: All drives + your custom folders")
            print("🚫 Excluded: D:\\ai_file_manager")
        return
    
    if args.start:
        print("🚀 Starting AI File Manager Automation...")
        controller = AutomationController()
        controller.start_automation()
    elif args.run:
        if args.run == 'organize':
            print("📁 Organizing ALL drives and folders...")
            organizer = AutoOrganizer()
            result = organizer.organize_all_drives()
            print(f"✅ {result}")
        elif args.run == 'cleanup':
            print("🧹 Cleaning temporary files across ALL drives...")
            cleaner = DiskCleaner()
            result = cleaner.clean_temp_files_all_drives()
            print(f"✅ {result}")
        elif args.run == 'backup':
            print("💾 Running FULL SYSTEM backup...")
            backup = BackupManager()
            result = backup.backup_all_drives()
            print(f"✅ {result}")
    else:
        print("🤖 AI File Manager - MULTI-DRIVE SUPPORT")
        print("=" * 50)
        print("Usage:")
        print("  python start_manager.py --start               # Start automated service")
        print("  python start_manager.py --run organize        # Organize ALL drives now")
        print("  python start_manager.py --run cleanup         # Clean ALL drives now") 
        print("  python start_manager.py --run backup          # Backup entire system now")
        print("  python start_manager.py --show-drives         # Show monitored locations")
        print()
        print("📀 Monitored: ALL drives (C:, D:, E:, etc.)")
        print("📁 Plus: Downloads, Desktop, Documents, etc.")
        print("🎯 And your custom folders on D: drive")

if __name__ == "__main__":
    main()
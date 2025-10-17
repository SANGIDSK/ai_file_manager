# automation_controller.py
import time
import schedule
import threading
from pathlib import Path
import logging

try:
    from auto_organizer import AutoOrganizer
    from disk_cleaner import DiskCleaner
    from backup_manager import BackupManager
    from config import config
except ImportError:
    # Fallback if other files don't exist yet
    pass

class AutomationController:
    def __init__(self):
        self.setup_logging()
        self.running = False
        
        # Initialize components
        try:
            self.organizer = AutoOrganizer()
            self.cleaner = DiskCleaner()
            self.backup = BackupManager()
        except:
            # Use dummy components if real ones aren't available
            self.organizer = DummyOrganizer()
            self.cleaner = DummyCleaner()
            self.backup = DummyBackup()
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        self.logger = logging.getLogger()
    
    def start_automation(self):
        """Start the automation service"""
        self.logger.info("🚀 Starting AI File Manager Automation")
        self.running = True
        
        # Schedule tasks
        self.schedule_tasks()
        
        # Start scheduler in background thread
        def run_scheduler():
            while self.running:
                schedule.run_pending()
                time.sleep(60)
        
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.daemon = True
        scheduler_thread.start()
        
        self.logger.info("✅ Automation running. Press Ctrl+C to stop.")
        
        # Keep main thread alive
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_automation()
    
    def schedule_tasks(self):
        """Schedule all automated tasks"""
        # Organize every 2 hours
        schedule.every(2).hours.do(self.organize_task)
        
        # Daily cleanup at 2 AM
        schedule.every().day.at("02:00").do(self.cleanup_task)
        
        # Backup at 1 AM daily
        schedule.every().day.at("01:00").do(self.backup_task)
        
        self.logger.info("📅 Scheduled: Organize every 2h, Backup at 1AM, Cleanup at 2AM")
    
    def organize_task(self):
        """Organize all drives"""
        self.logger.info("📁 Organizing all drives...")
        try:
            result = self.organizer.organize_all_drives()
            self.logger.info(f"✅ {result}")
        except Exception as e:
            self.logger.error(f"Organization failed: {e}")
    
    def cleanup_task(self):
        """Cleanup across all drives"""
        self.logger.info("🧹 Cleaning all drives...")
        try:
            result = self.cleaner.clean_temp_files_all_drives()
            self.logger.info(f"✅ {result}")
        except Exception as e:
            self.logger.error(f"Cleanup failed: {e}")
    
    def backup_task(self):
        """Backup all drives"""
        self.logger.info("💾 Backing up all drives...")
        try:
            result = self.backup.backup_all_drives()
            self.logger.info(f"✅ {result}")
        except Exception as e:
            self.logger.error(f"Backup failed: {e}")
    
    def stop_automation(self):
        """Stop the automation service"""
        self.running = False
        schedule.clear()
        self.logger.info("✅ Automation service stopped")

# Dummy classes for fallback
class DummyOrganizer:
    def organize_all_drives(self):
        return "Dummy organizer - no files processed"

class DummyCleaner:
    def clean_temp_files_all_drives(self):
        return "Dummy cleaner - no files cleaned"

class DummyBackup:
    def backup_all_drives(self):
        return "Dummy backup - no files backed up"
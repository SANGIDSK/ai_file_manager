# disk_cleaner.py
from pathlib import Path
import os

try:
    from config import config
except ImportError:
    class FallbackConfig:
        def get_all_drives(self):
            return ['C:\\']
    config = FallbackConfig()

class DiskCleaner:
    def clean_temp_files_all_drives(self):
        """Clean temp files across all drives"""
        total_cleaned = 0
        
        for drive in config.monitored_drives:
            cleaned = self.clean_drive_temp_files(drive)
            total_cleaned += cleaned
        
        return f"Cleaned {total_cleaned} temp files across all drives"
    
    def clean_drive_temp_files(self, drive_path):
        """Clean temp files on a specific drive"""
        drive = Path(drive_path)
        cleaned_files = 0
        
        # Only clean known temp locations to be safe
        temp_locations = [
            drive / 'Windows' / 'Temp',
            drive / 'Temp',
            Path.home() / 'AppData' / 'Local' / 'Temp'
        ]
        
        for temp_dir in temp_locations:
            if temp_dir.exists():
                for file_path in temp_dir.glob('*'):
                    if file_path.is_file():
                        try:
                            file_path.unlink()
                            cleaned_files += 1
                        except:
                            pass
        
        return cleaned_files
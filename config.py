# config.py
from pathlib import Path
import os
import string

class Config:
    def __init__(self):
        self.monitored_drives = self.get_all_drives()
        self.monitored_folders = self.get_important_folders()
        self.custom_folders = self.get_custom_folders()  # Your specific folders
        
    def get_all_drives(self):
        """Get all available drives on the system"""
        drives = []
        for drive in string.ascii_uppercase:
            drive_path = f"{drive}:\\"
            if os.path.exists(drive_path):
                drives.append(drive_path)
        return drives
    
    def get_important_folders(self):
        """Get important user folders to monitor"""
        home = Path.home()
        important_folders = [
            str(home / "Downloads"),
            str(home / "Desktop"), 
            str(home / "Documents"),
            str(home / "Pictures"),
            str(home / "Videos"),
            str(home / "Music"),
        ]
        return [f for f in important_folders if Path(f).exists()]
    
    def get_custom_folders(self):
        """Get your specific folders from D: drive"""
        custom_folders = [
            "D:\\Games",                # Games folder
            "D:\\my certificates",      # Certificates
            "D:\\notepad",              # Notepad files
            "D:\\sangi",                # Personal folder
            "D:\\TeraBoxDownload",      # Download folder
            "D:\\tutorial"              # Tutorials
        ]
        # Only include folders that actually exist
        return [f for f in custom_folders if Path(f).exists()]
    
    def get_all_monitored_paths(self):
        """Combine drives, folders, and custom folders for complete monitoring"""
        all_paths = self.monitored_drives + self.monitored_folders + self.custom_folders
        # Remove duplicates and non-existent paths
        return list(set([p for p in all_paths if Path(p).exists()]))

# Global config instance
config = Config()
# backup_manager.py
import shutil
from datetime import datetime
from pathlib import Path

try:
    from config import config
except ImportError:
    class FallbackConfig:
        def get_important_folders(self):
            return [str(Path.home() / "Downloads")]
    config = FallbackConfig()

class BackupManager:
    def backup_all_drives(self):
        """Backup important folders"""
        dest_path = Path.home() / "Backups" / f"Backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        dest_path.mkdir(parents=True, exist_ok=True)
        
        backed_up = 0
        for folder in config.monitored_folders:
            source_path = Path(folder)
            if source_path.exists():
                backed_up += self.safe_backup_folder(source_path, dest_path / source_path.name)
        
        return f"Backed up {backed_up} files to {dest_path}"
    
    def safe_backup_folder(self, source, destination):
        """Safely backup a folder"""
        copied_count = 0
        for file_path in source.rglob('*'):
            if file_path.is_file():
                try:
                    rel_path = file_path.relative_to(source)
                    dest_path = destination / rel_path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, dest_path)
                    copied_count += 1
                except:
                    pass
        return copied_count
# auto_organizer.py
import shutil
from pathlib import Path

try:
    from config import config
except ImportError:
    # Fallback config
    class FallbackConfig:
        def get_all_monitored_paths(self):
            return [str(Path.home() / "Downloads")]
    config = FallbackConfig()

class AutoOrganizer:
    def __init__(self):
        ## order to organize files (can change the order in according to preference)
        self.rules = {
            'Images': ['.jpg', '.png', '.gif', '.jpeg', '.bmp', '.svg', '.webp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx'],
            'Archives': ['.zip', '.rar', '.7z', '.tar'],
            'Code': ['.py', '.js', '.html', '.css', '.java'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Video': ['.mp4', '.avi', '.mov'],
            'Executables': ['.exe', '.msi'],
        }
    
    def organize_all_drives(self):
        """Organize files across all drives and folders"""
        total_organized = 0
        locations_organized = []
        
        for path in config.get_all_monitored_paths():
            try:
                result = self.organize_folder(path, verbose=False)
                # Extract number from result string
                if "Organized" in result:
                    parts = result.split()
                    if len(parts) > 1 and parts[1].isdigit():
                        count = int(parts[1])
                        if count > 0:
                            total_organized += count
                            locations_organized.append(f"{Path(path).name}: {count} files")
            except Exception as e:
                continue
        
        if locations_organized:
            return f"Organized {total_organized} files across {len(locations_organized)} locations"
        else:
            return "No files needed organization"
    
    def organize_folder(self, folder_path, verbose=True):
        folder = Path(folder_path)
        if not folder.exists():
            return f"Folder not found: {folder_path}"
        
        moved_count = 0
        for item in folder.glob('*'):
            if item.is_file():
                category = self.get_file_category(item)
                if category != 'Other':
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(item), str(target_dir / item.name))
                        moved_count += 1
                    except:
                        pass
        
        return f"Organized {moved_count} files in {folder_path}"
    
    def get_file_category(self, file_path):
        ext = file_path.suffix.lower()
        for category, extensions in self.rules.items():
            if ext in extensions:
                return category
        return 'Other'
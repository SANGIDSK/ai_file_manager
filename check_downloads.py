# check_downloads.py
from pathlib import Path

def analyze_downloads():
    downloads = Path.home() / 'Downloads'
    print(f"🔍 Analyzing: {downloads}")
    
    if not downloads.exists():
        print("❌ Downloads folder doesn't exist!")
        return
    
    files = list(downloads.glob('*'))
    print(f"📊 Total items: {len(files)}")
    
    file_count = 0
    folder_count = 0
    file_types = {}
    
    for item in files:
        if item.is_file():
            file_count += 1
            ext = item.suffix.lower()
            file_types[ext] = file_types.get(ext, 0) + 1
            print(f"📄 {item.name} ({(item.stat().st_size / 1024):.1f} KB)")
        elif item.is_dir():
            folder_count += 1
            print(f"📁 {item.name}/")
    
    print(f"\n📈 Summary: {file_count} files, {folder_count} folders")
    print("📋 File extensions found:", file_types)

if __name__ == "__main__":
    analyze_downloads()

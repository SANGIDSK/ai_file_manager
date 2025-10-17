# delete_test_files.py
from pathlib import Path
import shutil

def cleanup_downloads():
    downloads = Path.home() / 'Downloads'
    print("🧹 Cleaning up test files...")
    
    # List of test files we created
    test_files = [
        'sample_image.jpg', 'document.pdf', 'spreadsheet.xlsx',
        'python_script.py', 'music_file.mp3', 'video_clip.mp4',
        'archive.zip', 'text_file.txt', 'presentation.pptx', 'data.csv'
    ]
    
    deleted_count = 0
    
    # Delete individual test files
    for filename in test_files:
        file_path = downloads / filename
        if file_path.exists():
            file_path.unlink()
            print(f"✅ Deleted {filename}")
            deleted_count += 1
    
    # Delete organized folders (if they exist)
    folders_to_delete = ['Images', 'Documents', 'Spreadsheets', 'Code', 
                        'Audio', 'Video', 'Archives', 'Presentations', 'Data']
    
    for folder_name in folders_to_delete:
        folder_path = downloads / folder_name
        if folder_path.exists() and folder_path.is_dir():
            shutil.rmtree(folder_path)
            print(f"✅ Deleted folder {folder_name}/")
            deleted_count += 1
    
    print(f"🎯 Cleanup complete! Deleted {deleted_count} items")

if __name__ == "__main__":
    cleanup_downloads()

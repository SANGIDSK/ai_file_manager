# create_test_files.py
from pathlib import Path
import os

def create_test_downloads():
    downloads = Path.home() / 'Downloads'
    
    # Create sample files of different types
    test_files = {
        'sample_image.jpg': b'fake image content',
        'document.pdf': b'fake pdf content', 
        'spreadsheet.xlsx': b'fake excel content',
        'python_script.py': b'print("Hello World")',
        'music_file.mp3': b'fake audio content',
        'video_clip.mp4': b'fake video content',
        'archive.zip': b'fake zip content',
        'text_file.txt': b'This is a text file',
        'presentation.pptx': b'fake powerpoint content',
        'data.csv': b'name,age\nJohn,25\nJane,30'
    }
    
    print("📁 Creating test files in Downloads...")
    
    for filename, content in test_files.items():
        file_path = downloads / filename
        with open(file_path, 'wb') as f:
            f.write(content)
        print(f"✅ Created {filename}")
    
    print(f"\n🎯 Created {len(test_files)} test files")
    print("📁 Now run: python start_manager.py --run organize")

if __name__ == "__main__":
    create_test_downloads()

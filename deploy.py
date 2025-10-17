#!/usr/bin/env python3
"""
Script to copy EDCoPilot files one level up
Copies EDCoPilot.SpeechExtensions.Custom.txt and Pronunciations.txt
to the parent directory, overwriting existing files without prompting.
"""

import shutil
from pathlib import Path

print("🚀 Starting file copy operation...")

def copy_files():
    """Copy the specified files one directory level up"""
    
    # Get current script directory
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    
    # Define files to copy
    files_to_copy = [
        "EDCoPilot.SpeechExtensions.Custom.txt",
        "Pronunciations.txt"
    ]
    
    print(f"📁 Source directory: {current_dir}")
    print(f"📂 Target directory: {parent_dir}")
    print()
    
    success_count = 0
    
    for filename in files_to_copy:
        source_file = current_dir / filename
        target_file = parent_dir / filename
        
        try:
            # Check if source file exists
            if not source_file.exists():
                print(f"❌ Source file not found: {filename}")
                continue
            
            # Copy file (this will overwrite existing files)
            shutil.copy2(source_file, target_file)
            print(f"✅ Copied: {filename}")
            success_count += 1
            
        except Exception as e:
            print(f"❌ Error copying {filename}: {str(e)}")
    
    print()
    print(f"📊 Summary: {success_count}/{len(files_to_copy)} files copied successfully")
    
    if success_count == len(files_to_copy):
        print("🎉 All files copied successfully!")
    elif success_count > 0:
        print("⚠️ Some files copied, but there were errors")
    else:
        print("💥 No files were copied")

if __name__ == "__main__":
    copy_files()
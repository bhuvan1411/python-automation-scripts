import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    try:
        # Ensure source folder exists
        if not os.path.exists(source_dir):
            print(f"❌ Source folder does not exist: {source_dir}")
            return
        
        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Create timestamped folder name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destination = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(destination)

        # Copy all files from source to destination
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(destination, item)

            if os.path.isfile(source_path):
                shutil.copy2(source_path, dest_path)
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
        
        print(f"✅ Backup created successfully at: {destination}")

    except Exception as e:
        print(f"❌ Error during backup: {e}")

if __name__ == "__main__":
    # Example: Back up all scripts from PROJECTS folder
    source_folder = os.path.join(os.getcwd(), "PROJECTS")

    backup_folder = os.path.join(os.getcwd(), "BACKUPS")

    create_backup(source_folder, backup_folder)

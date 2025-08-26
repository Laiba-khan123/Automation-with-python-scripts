import os
import shutil

# Source and destination folders
source_folder = "C:/Users/abcqw/Downloads"
destination_folder = "C:/Users/abcqw/Pictures/JPG_Files"

# Create destination folder if it doesn’t exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source_folder, file),
                    os.path.join(destination_folder, file))
        print(f"Moved: {file}")

print("✅ All JPG files moved successfully!")

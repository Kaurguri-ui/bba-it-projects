# automation_script.py
# Simple Python script to rename files in a folder

import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for count, filename in enumerate(files):
        new_name = f"file_{count + 1}.txt"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
    print(f"Renamed {len(files)} files.")

# Example usage: change 'your_folder' to the folder you want to rename files in
if __name__ == "__main__":
    folder = "your_folder"
    rename_files(folder)

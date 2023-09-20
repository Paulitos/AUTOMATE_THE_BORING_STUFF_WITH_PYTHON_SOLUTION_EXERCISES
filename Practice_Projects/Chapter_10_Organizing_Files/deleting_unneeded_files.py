# Deleting Unneeded Files Page 247 Chapter 10
import os

def find_large_files(folder_path, size_limit):
    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                # Get the file size in bytes
                file_size = os.path.getsize(file_path)
                # Convert file size to megabytes (MB)
                file_size_mb = file_size / (1024 * 1024)
                if file_size_mb > size_limit:
                    print(f"Large file found: {file_path} ({file_size_mb:.2f} MB)")
            except OSError as e:
                print(f"Error accessing {file_path}: {e}")

# Set the folder path and size limit (in MB)
folder_path = r"C:\Users\pablo\Documents\Github_repo_AUTOMATING_THE_BORING_STUFF_WITH_PYTHON\Practice_Projects\Chapter_10_Organizing_Files\Folder_with_big_files"
size_limit_mb = 100

find_large_files(folder_path, size_limit_mb)

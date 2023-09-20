# Selective Copy Page 247 Chapter 10
import os
import shutil

def copy_files_by_extension(source_folder, destination_folder, file_extension):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the source folder and its subdirectories
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(file_extension):
                source_file = os.path.join(foldername, filename)
                destination_file = os.path.join(destination_folder, filename)

                # Copy the file to the destination folder
                shutil.copy(source_file, destination_file)
                print(f"Copied {source_file} to {destination_file}")

# Example usage:
source_folder = r"C:\Users\pablo\Documents\Github_repo_AUTOMATING_THE_BORING_STUFF_WITH_PYTHON\Practice_Projects\Chapter_10_Organizing_Files\Source_folder"
destination_folder = r"C:\Users\pablo\Documents\Github_repo_AUTOMATING_THE_BORING_STUFF_WITH_PYTHON\Practice_Projects\Chapter_10_Organizing_Files\Destination_folder"
file_extension = '.jpg'  # Change this to the desired file extension

copy_files_by_extension(source_folder, destination_folder, file_extension)


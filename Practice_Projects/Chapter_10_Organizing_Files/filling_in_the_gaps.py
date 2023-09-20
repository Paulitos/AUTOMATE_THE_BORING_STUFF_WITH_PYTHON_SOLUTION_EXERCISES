# Filling in the Gaps Page 248 Chapter 10
import os
import re

def close_numbering_gaps(folder, prefix):
    # Get a list of all files in the folder
    all_files = os.listdir(folder)

    # Create a regex pattern to match the prefix and numbering
    pattern = re.compile(rf'{re.escape(prefix)}(\d+)(\..*)')

    # Find all matching files and extract their numbers
    file_numbers = []
    for filename in all_files:
        match = pattern.match(filename)
        if match:
            file_numbers.append(int(match.group(1)))

    if not file_numbers:
        print(f"No files found with the prefix '{prefix}' in the folder.")
        return

    # Sort the file numbers
    file_numbers.sort()

    # Rename files to close numbering gaps
    for i, number in enumerate(file_numbers):
        new_filename = f'{prefix}{i+1:03d}{match.group(2)}'
        old_filename = f'{prefix}{number:03d}{match.group(2)}'
        if new_filename != old_filename:
            print(f'Renaming "{old_filename}" to "{new_filename}"')
            os.rename(os.path.join(folder, old_filename), os.path.join(folder, new_filename))

# Example usage:
folder_path = r"C:\Users\pablo\Documents\Github_repo_AUTOMATING_THE_BORING_STUFF_WITH_PYTHON\Practice_Projects\Chapter_10_Organizing_Files\Folder_for_filling_the_gaps"
file_prefix = 'spam'

close_numbering_gaps(folder_path, file_prefix)


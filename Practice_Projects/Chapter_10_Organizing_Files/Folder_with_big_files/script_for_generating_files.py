# Small program to test the deleting_unneeded_files.py
import os

# Define file sizes in bytes
file_sizes_bytes = [150 * 1024 * 1024, 100 * 1024 * 1024, 50 * 1024 * 1024]

# Specify the file paths for each file
file_paths = ["large_file_150MB.dat", "large_file_100MB.dat", "large_file_50MB.dat"]

for file_size_bytes, file_path in zip(file_sizes_bytes, file_paths):
    # Generate random data to fill the file
    data = os.urandom(file_size_bytes)

    # Write the data to the file
    with open(file_path, "wb") as file:
        file.write(data)

    print(f"Created a {file_size_bytes / (1024 * 1024):.2f} MB file at '{file_path}'")


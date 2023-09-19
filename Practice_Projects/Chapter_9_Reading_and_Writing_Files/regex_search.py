# Regex Search Page 230 Chapter 9
import os
import re

# Prompt the user for a regular expression to search for
user_regex = input("Enter a regular expression to search for: ")

# Define a function to search for the regex pattern in a file
def search_file(file_path, regex):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if re.search(regex, line):
                print(f'File: {file_path}, Line: {line_number}, Content: {line.strip()}')

# Specify the folder containing the .txt files
folder_path = '.'  # Change this to your folder path

# Iterate through all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        search_file(file_path, re.compile(user_regex))



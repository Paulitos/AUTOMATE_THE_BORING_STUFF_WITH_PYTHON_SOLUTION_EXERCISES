# Text Files to Spreadsheet Page 328 Chapter 13
import openpyxl

# List of text file names to read
text_files = ["file1.txt", "file2.txt", "file3.txt"]  # Add your file names here

# Create a new Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Loop through the text files and insert their contents into columns
for col, filename in enumerate(text_files, 1):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for row, line in enumerate(lines, 1):
            sheet.cell(row=row, column=col, value=line.strip())

# Save the workbook with a specific name (e.g., 'output.xlsx')
wb.save('output_textFiles_toSpreadsheet.xlsx')

# Close the workbook
wb.close()


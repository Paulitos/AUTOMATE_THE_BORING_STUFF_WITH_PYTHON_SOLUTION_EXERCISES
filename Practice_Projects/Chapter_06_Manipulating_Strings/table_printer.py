# Table Printer Page 154 Chapter 6
def printTable(tableData):
    # Initialize a list to store the maximum width of each column
    colWidths = [0] * len(tableData)

    # Find the maximum width for each column
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    # Determine the number of rows and columns
    numRows = len(tableData[0])
    numCols = len(tableData)

    # Print the table with right-justified columns
    for row in range(numRows):
        for col in range(numCols):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()

# Example data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Call the function to print the table
printTable(tableData)

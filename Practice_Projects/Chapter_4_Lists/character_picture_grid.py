# Character Picture Grid Page 108 Chapter 4
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Calculate the dimensions of the rotated grid
num_rows = len(grid)
num_cols = len(grid[0])

# Create a new grid for the rotated image
rotated_grid = [[' ' for _ in range(num_rows)] for _ in range(num_cols)]

# Rotate the original grid 45º clockwise
for x in range(num_rows):
    for y in range(num_cols):
        rotated_grid[y][num_rows - 1 - x] = grid[x][y]

# Print the rotated grid
for row in rotated_grid:
    print(' '.join(row))



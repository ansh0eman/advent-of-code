with open("inputs/day04.txt", "r") as f:
    lines = f.read()

# Construct the grid
grid = [list(row.strip()) for row in lines.split()]
rows, cols = len(grid), len(grid[0])
count = 0

# frame of reference is 3x3 square with center from (1,1) to (n-1,n-1) for griday of size n
# M . M  |  S . S  |  M . S  |  S . M
# . A .  |  . A .  |  . A .  |  . A .
# S . S  |  M . M  |  M . S  |  S . M
count = 0
for i in range(1, len(grid) - 1):
  for j in range(1, len(grid) - 1):
    if grid[i][j] == 'A':  # short circuit - center is A
      if ((grid[i-1][j-1] == 'M' and grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'S') or  # M on top, S on bottom
          (grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S' and grid[i-1][j+1] == 'S') or  # M on bottom, S on top
          (grid[i-1][j-1] == 'M' and grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S' and grid[i+1][j+1] == 'S') or  # M on left, S on right
          (grid[i-1][j+1] == 'M' and grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S' and grid[i+1][j-1] == 'S')):   # M on right, S on left
        count += 1

print(count)

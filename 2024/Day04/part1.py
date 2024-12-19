with open("inputs/day04.txt", "r") as f:
    lines = f.read()

grid = [list(row.strip()) for row in lines.split()]
word = "XMAS"
rows, cols = len(grid), len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
count = 0

def dfs(x, y, index, direction):
    if index == len(word):
        return True  # Found a full match

    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != word[index]:
        return False  # Out of bounds or letter mismatch

    temp = grid[x][y]  # Save current letter
    grid[x][y] = "."  # Temporarily mark as visited

    found = False
    dx, dy  = direction[0], direction[1]
    if dfs(x + dx, y + dy, index + 1, direction):
        found = True

    grid[x][y] = temp  
    return found

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'X':
            for direction in directions:    # Search in Specific directions only one at a time
                if dfs(i, j, 0, direction): 
                  count += 1

print(count)

def turn_right(direction):
    keys = ['^', '>', 'v', '<']
    return keys[(keys.index(direction) + 1) % 4]

def move_guard(grid, start_x, start_y, start_dir):
    m, n = len(grid), len(grid[0])
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    visited_states = set()
    x, y, direction = start_x, start_y, start_dir

    while 0 <= x < m and 0 <= y < n:
        state = (x, y, direction)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '#':
            direction = turn_right(direction)
        else:
            x, y = nx, ny

    return False  # Guard exits the map

def count_valid_obstruction_positions(grid):
    m, n = len(grid), len(grid[0])
    directions = {'^', '>', 'v', '<'}
    start_x, start_y, start_dir = None, None, None

    # Find the guard's starting position and direction
    for i in range(m):
        for j in range(n):
            if grid[i][j] in directions:
                start_x, start_y, start_dir = i, j, grid[i][j]
                break
        if start_x is not None:
            break

    valid_positions = 0

    # Test each empty position (.) for placing an obstruction
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.' and (i, j) != (start_x, start_y):
                # Temporarily place obstruction
                grid[i][j] = '#'
                if move_guard(grid, start_x, start_y, start_dir):
                    valid_positions += 1
                # Remove obstruction
                grid[i][j] = '.'

    return valid_positions

# Input processing
with open("inputs/day06.txt", "r") as f:
    lines = f.read().splitlines()

grid = [list(line) for line in lines]
# print(grid)
result = count_valid_obstruction_positions(grid)
print(result)

def parse_input(input_grid):
    antennas = {}
    for row, line in enumerate(input_grid.strip().split("\n")):
        for col, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((row, col))
    return antennas

def calculate_antinodes(antennas, grid_size):
    antinodes = set()
    rows, cols = grid_size
    
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                ax, ay = positions[i]
                bx, by = positions[j]
                
                # Calculate potential antinodes
                dx, dy = bx - ax, by - ay
                
                # Antinode 1
                nx1, ny1 = ax - dx, ay - dy
                if 0 <= nx1 < rows and 0 <= ny1 < cols:
                    antinodes.add((nx1, ny1))
                
                # Antinode 2
                nx2, ny2 = bx + dx, by + dy
                if 0 <= nx2 < rows and 0 <= ny2 < cols:
                    antinodes.add((nx2, ny2))
    
    return antinodes

def count_unique_antinodes(input_grid):
    grid = input_grid.strip().split("\n")
    rows, cols = len(grid), len(grid[0])
    antennas = parse_input(input_grid)
    antinodes = calculate_antinodes(antennas, (rows, cols))
    return len(antinodes)

with open('inputs/day08.txt', 'r') as f:
    input_grid = f.read()

# Solve
print(count_unique_antinodes(input_grid))

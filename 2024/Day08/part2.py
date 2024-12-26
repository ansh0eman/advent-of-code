from math import gcd
from itertools import combinations

def parse_input(input_grid):
    """
    Parse the input grid and group antenna coordinates by frequency.
    """
    antennas = {}
    for row, line in enumerate(input_grid.strip().split("\n")):
        for col, char in enumerate(line):
            if char != ".":  # Antenna is represented by any character other than '.'
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((row, col))
    return antennas

def generate_antinodes(coord1, coord2, rows, cols):
    """
    Generate all antinodes along the line connecting two coordinates, 
    including extrapolated points within grid boundaries.
    """
    x1, y1 = coord1
    x2, y2 = coord2

    # Calculate direction vector (dx, dy) reduced to smallest step
    dx = x2 - x1
    dy = y2 - y1
    step = gcd(abs(dx), abs(dy))
    dx //= step
    dy //= step

    # Generate points between and beyond the two coordinates
    antinodes = set()

    # Forward direction from coord1
    x, y = x1, y1
    while 0 <= x < rows and 0 <= y < cols:
        antinodes.add((x, y))
        x += dx
        y += dy

    # Backward direction from coord2
    x, y = x2, y2
    while 0 <= x < rows and 0 <= y < cols:
        antinodes.add((x, y))
        x -= dx
        y -= dy

    return antinodes

def calculate_antinodes_v2(antennas, grid_size):
    """
    Calculate all unique antinodes for all antenna pairs within the grid.
    """
    antinodes = set()
    rows, cols = grid_size

    for freq, positions in antennas.items():
        # Add all antenna positions as antinodes
        antinodes.update(positions)

        # Generate antinodes for each pair of antennas
        for pair in combinations(positions, 2):
            antinodes.update(generate_antinodes(pair[0], pair[1], rows, cols))

    return antinodes

def count_unique_antinodes_v2(input_grid):
    """
    Count unique antinodes generated from the input grid.
    """
    grid = input_grid.strip().split("\n")
    rows, cols = len(grid), len(grid[0])
    antennas = parse_input(input_grid)
    antinodes = calculate_antinodes_v2(antennas, (rows, cols))
    return len(antinodes)

with open('inputs/day08.txt', 'r') as f:
    input_grid = f.read()
# Solve
print(count_unique_antinodes_v2(input_grid))  # Outputs the total unique antinodes

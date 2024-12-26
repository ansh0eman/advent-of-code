def parse_input(disk_map):
    """Parses the disk map input into a list of (length, id) pairs."""
    antennas = []
    i = 0
    while i < len(disk_map):
        length = int(disk_map[i])
        antennas.append((length, len(antennas)))  # Store (length, file ID)
        i += 1
    
    return antennas

def compact_disk(antennas):
    """Compacts the disk by moving files left into free spaces."""
    total_blocks = sum(length for length, _ in antennas)
    disk = ['.'] * total_blocks  # Initialize disk with free spaces
    idx = 0  # Position to place the next file block

    for length, file_id in antennas:
        for _ in range(length):
            disk[idx] = str(file_id)  # Place the file ID in the disk
            idx += 1  # Move to the next position
    
    return disk

def calculate_checksum(disk):
    """Calculates the filesystem checksum based on the compacted disk."""
    checksum = 0
    for position, block in enumerate(disk):
        if block != '.':
            checksum += position * int(block)  # Multiply position by file ID
    return checksum

def solve(disk_map):
    antennas = parse_input(disk_map)
    disk = compact_disk(antennas)
    checksum = calculate_checksum(disk)
    return checksum

# Example Input
input_disk_map = "2333133121414131402"  # Replace with the actual puzzle input for testing

# Solve
result = solve(input_disk_map)
print("Resulting Filesystem Checksum:", result)

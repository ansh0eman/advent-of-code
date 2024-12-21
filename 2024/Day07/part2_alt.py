from itertools import product

# Read input
with open("inputs/day07.txt", "r") as f:
    lines = f.read().strip().split('\n')

# Parse input
equations = []
for line in lines:
    target, nums = line.split(':')
    target = int(target.strip())
    nums = list(map(int, nums.strip().split()))
    equations.append((target, nums))

def evaluate_expression(numbers, operators):
    """Evaluate the expression left-to-right using the given operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '*':
            result *= numbers[i + 1]
        elif op == '+':
            result += numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))  # Handle concatenation
    return result

def solve(part2):
    total = 0
    for target, numbers in equations:
        n = len(numbers)
        valid = False
        
        # Define all operators for Part 1 or Part 2
        all_ops = ['+', '*']
        if part2:
            all_ops.append('||')  # Add concatenation for Part 2

        # Generate all possible operator combinations
        for operators in product(all_ops, repeat=n - 1):
            # Evaluate expression with current operator combination
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break

        # Add to total if valid
        if valid:
            total += target
    return total

# Solve Part 1
print("Part 1:", solve(part2=False))

# Solve Part 2
print("Part 2:", solve(part2=True))

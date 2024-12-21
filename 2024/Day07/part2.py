from itertools import product

with open("inputs/day07.txt", "r") as f:
    lines = f.read().split('\n')

equations = []
for line in lines:
    target, nums = line.split(':')
    target = int(target.strip())
    nums = list(map(int,nums.strip().split()))
    equations.append((target, nums))

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i,op in enumerate(operators):
        if(op =='*'):
            result *= numbers[i+1]
        elif(op == '+'):
            result += numbers[i+1]
        elif(op == '||'):
            result = int(str(result) + str(numbers[i+1]))
    return result

# operators = ['+', '*']
# result = product(operators, repeat=1)
# print(list(result))

def solve(part2):
    total = 0
    for target, numbers in equations:
        n = len(numbers)
        valid = False
        all_ops = ['+', '*']

        if(part2):
            all_ops.append('||')

        for operators in product(all_ops, repeat = n-1):
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break
        if valid == True:
            total += target
    return total

print(solve(part2=True))
     
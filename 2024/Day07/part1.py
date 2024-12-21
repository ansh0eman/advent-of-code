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
    return result

total = 0

# operators = ['+', '*']
# result = product(operators, repeat=1)
# print(list(result))

for target, numbers in equations:
    n = len(numbers)
    valid = False
    for operators in product(['*','+'], repeat= n-1):
        if evaluate_expression(numbers, operators) == target:
            valid = True
            break
    if valid == True:
        total += target

print(total)
     
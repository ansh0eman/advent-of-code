import re

with open('inputs/day03.txt', "r") as f:
    lines = f.read()

# remove everything between don't() and do() or between don't() and EOF
input_data = re.sub(r"don't\(\).*?(?:do\(\)|$)", "", lines, flags=re.DOTALL)

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_data)  # extract tuples of numbers to multiply

# print(matches)

print(sum([int(match[0])*int(match[1]) for match in matches]))

with open('inputs/day01.txt',"r") as f:
    lines = f.readlines()

a = []
b = []

for line in lines:
    a.append(int(line.split()[0].strip()))
    b.append(int(line.split()[1].strip()))

t = 0

for num in a:
    t += num * b.count(num)

print(t)
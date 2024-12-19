with open('inputs/day01.txt',"r") as f:
    lines = f.readlines()

a = []
b = []

for line in lines:
    a.append(int(line.split()[0].strip()))
    b.append(int(line.split()[1].strip()))

a.sort()
b.sort()

t=0

for i in range(len(a)):
    t+= abs(a[i] - b[i])

print(t)

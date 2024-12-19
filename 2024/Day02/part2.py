with open('inputs/day02.txt', "r") as f:
    lines = f.readlines()

def isSafe(a):
    diff = [a[i+1] - a[i] for i in range(len(a)-1)]
    if(all(x > 0 and x in range(1,4) for x in diff) or
       all(x < 0 and x in range(-3,0) for x in diff)):
        
        return True
    else: 
        return False

def isSafeWithDampner(a):

    if(isSafe(a)): return True

    for i in range(len(a)):
        temp = []
        for j in range(len(a)):
            if(i != j):
                temp.append(a[j])
        if(isSafe(temp)):
            return True
    return False         

count = 0

for line in lines:
    report = [int(x.strip()) for x in line.split()]
    if isSafeWithDampner(report):
        count += 1

print(count)

# for line in lines:
#     report = [int(x.strip()) for x in line.split()]
#     if isSafe(report):
#         count+=1
#     else:
#         for i in range(len(report)):
#             temp_report = report.copy()
#             temp_report.pop(i)
#             if(isSafe(temp_report)):
#                 count+=1
#                 break




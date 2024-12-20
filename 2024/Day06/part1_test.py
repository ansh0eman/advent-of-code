## ONLY WORKS WITH TEST DATA
## RECURSION ERROR --> MAX RECURSION DEPTH EXCEEDED

with open("../inputs/day06_test.txt", "r") as f:
    lines = f.read().split('\n')

# grid = []
# for line in lines:
#     arr = []
#     for ch in line:
#         arr.append(ch)
#     grid.append(arr)


grid = [list(line) for line in lines]
m,n = len(grid), len(grid[0])
directions= {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}
keys = list(directions.keys())

def print_grid(grid):
    for i in range(m):
        print(grid[i])
    print('\n\n')

def turn_right(current_direction):
    index = (keys.index(current_direction) + 1) % len(keys)
    return keys[index]
 
def move(i, j, direction):

    if i < 0 or j < 0 or i >= m or j >= n: # out of bounds
        return
    
    dx, dy = i+directions[direction][0], j+directions[direction][1]

    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == '#': # obstacle --> TURN RIGHT
        direction = turn_right(direction)
        move(i,j, direction)
        return
    
    if 0 <= dx < m and 0 <= dy < n:
        grid[dx][dy] = 'X'
    print_grid(grid)
    move(dx, dy, direction)

        
for i in range(m):
    for j in range(n):
        if(grid[i][j] in directions.keys()):
            direction = grid[i][j]
            grid[i][j] = 'X'
            print_grid(grid)
            move(i,j,direction)


count =0
for i in range(m):
    for j in range(n):
        if(grid[i][j]=='X'):
            print('\n\n')
            count+=1
print(count)
#!/usr/bin/env python3

import sys

n = int(input())
if n < 1 or n >= 501:
    sys.exit()

grid = list()

for i in range(n):
    row = input().split()   #Getting str input and separating the numbers in each row
    rows = list()   # rows = int(row)
    for x in row:
        x = int(x)      # Turning str to int every item of each row and appending it to rows if this input number is acceptable
        if x >= 0 or x <= (10**9):
            rows.append(x) # Appending the int in a new list (rows)
        else:
            sys.exit()
        
    if len(rows) != n:  # Checking that the input in each row is equal to n. Meaning that the table is n X n
        sys.exit()
    grid.append(rows)  # Appending the lists rows in the list grid

print(grid)

# Done with forming the grid
# Now we need to check if two or more rows, columns and diagonals without containing 0 have the same sum
# and find the correct missing number or -1
if 0 in grid[0]:
    count = sum(grid[1])
else:
    count = sum(grid[0])

def row_check(table):

    for j in range(n):
        if 0 in table[j]:
            continue
        if sum(table[j]) != count:
            sys.exit()


def dia_check(table):
    total = 0
    for i in range(n):
        if 0 == table[i][i]:
            break
        total += table[i][i]
    if total != count:
        sys.exit()
    
    total = 0
    for i in reversed(range(n)):
        if 0 == table[i][i]:
            break
        total += table[i][i]
    if total != count:
        sys.exit()



def col_check(table):
    total = 0
    for i in range(n):
        for j in range(n):
            if 0 == table[j][i]:
                break
            total += table[j][i]
            if total != count:
                sys.exit()
def sth(table):
    total = 0
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if 0 == table[j][i]:
                break
            if total != count:
                sys.exit()




#print(row_check(grid))
#print(dia_check(grid))
print(col_check(grid))

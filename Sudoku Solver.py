from collections import deque

def checkValidity(x, y, num, puzzle):
    zipped = deque(zip(*puzzle))
    check = deque([])
    for row in range (len(puzzle)):
        check.append(puzzle[x][row])
    if num in check:
        return False
    check.clear()

    for col in range (len(puzzle)):
        check.append(zipped[y][col])
    if num in check:
        return False
    check.clear()

    for sqr_x in range(int(x/3)*3,(int(x/3)*3)+3):
        for sqr_y in range(int(y/3)*3,(int(y/3)*3)+3):
            check.append(puzzle[sqr_x][sqr_y])
    if num in check:
        return False
    
    return True


def findPattern(puzzle, store, pos):
    if pos == len(store):
        return True
    x = store[pos][0]
    y = store[pos][1]
    for num in range(1, 10):
        if checkValidity(x, y, num, puzzle):
            puzzle[x][y] = num
            if (findPattern(puzzle, store, pos+1)):
                return True
            else:
                puzzle[x][y] = 0
    
    return False

def sudoku(puzzle):
    store = deque([])
    n = len(puzzle)
    for x in range(n):
        for y in range(n):
            if puzzle[x][y] == 0:
                store.append((x, y))
    if findPattern(puzzle,store,0):
        return puzzle
    else:
        return "no possible solution"

    
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

puzzle = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,8,0,0,0,0]]         



# puzzle =[ [5 ,3, 4, 0, 7, 8, 9, 1, 2],
#           [6, 7, 2, 1, 9, 5, 3, 4, 8],
#           [1, 9, 8, 3, 4, 2, 5, 6, 7],
#           [8, 5, 9, 7, 6, 1, 4, 2, 3],
#           [4, 2, 6, 8, 5, 3, 7, 9, 1],
#           [7, 1, 3, 9, 2, 4, 8, 5, 6],
#           [9, 6, 1, 5, 3, 7, 2, 8, 4],
#           [2, 8, 7, 4, 1, 9, 6, 3, 5],
#           [3, 4, 5, 2, 8, 6, 1, 7, 9]  ]

print (sudoku(puzzle))


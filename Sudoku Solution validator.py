def valid_solution(board):
    for row in range (len(board)):
        row_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for col in range(len(board[row])):
            sqr_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            col_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if board[row][col] == 0:
                return False
            if board[row][col] in row_nums:
                row_nums.remove(board[row][col])
            else:
                return False
            
            if row % 3 == 0 and col % 3 == 0:
                for mini_row in range(row, row+3):
                    for mini_col in range(col, col+3):
                        if board[mini_row][mini_col] in sqr_nums:
                            sqr_nums.remove(board[mini_row][mini_col])
                        else:
                            return False
            
            if row == 1:
                for chck_col in range (len(board)):
                    if board[chck_col][col] in col_nums:
                        col_nums.remove(board[chck_col][col])
                    else:
                        return False
    return True

        
        
            



sudoku =   [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


print (valid_solution(sudoku))


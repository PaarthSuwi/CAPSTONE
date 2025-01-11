# def is_valid(board, row, col, num):
#     # Check if the number is not in the current row, column, or 3x3 subgrid
#     for i in range(9):
#         if board[row][i] == num or board[i][col] == num:
#             return False
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if board[start_row + i][start_col + j] == num:
#                 return False
#     return True

# def solve_sudoku(board):
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == 0:  # Find an empty cell
#                 for num in range(1, 10):  # Try numbers 1-9
#                     if is_valid(board, row, col, num):
#                         board[row][col] = num  # Place the number
#                         if solve_sudoku(board):  # Recursively solve the rest
#                             return True
#                         board[row][col] = 0  # Backtrack if the solution is invalid
#                 return False  # Trigger backtracking
#     return True  # Sudoku solved

# def print_board(board):
#     for row in board:
#         print(" ".join(str(num) if num != 0 else '.' for num in row))

# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# print("Sudoku Puzzle:")
# print_board(board)

# if solve_sudoku(board):
#     print("\nSolved Sudoku:")
#     print_board(board)
# else:
#     print("No solution exists.")

def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        row_set = set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
    
    # Check columns
    for j in range(9):
        col_set = set()
        for i in range(9):
            if board[i][j] != '.':
                if board[i][j] in col_set:
                    return False
                col_set.add(board[i][j])
    
    # Check 3x3 sub-boxes
    for block in range(9):
        box_set = set()
        for i in range(block // 3 * 3, block // 3 * 3 + 3):
            for j in range(block % 3 * 3, block % 3 * 3 + 3):
                if board[i][j] != '.':
                    if board[i][j] in box_set:
                        return False
                    box_set.add(board[i][j])
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.': 
                for num in map(str, range(1, 10)): 
                    if is_valid_placement(board, row, col, num):
                        board[row][col] = num  
                        if solve_sudoku(board):  
                            return True
                        board[row][col] = '.'  
                return False  
    return True  

def is_valid_placement(board, row, col, num):
    
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != '.' else '.' for num in row))

def input_sudoku_board():
    board = []
    print("Enter the Sudoku board row by row (use '.' for empty cells):")
    for i in range(9):
        row = input(f"Row {i+1}: ").strip()
        if len(row) != 9:
            print("Each row must have exactly 9 characters. Please try again.")
            return input_sudoku_board()
        board.append(list(row))
    return board

def main():
    board = input_sudoku_board()
    if is_valid_sudoku(board):
        print("\nThe Sudoku board is valid.")
        print("\nSudoku Puzzle:")
        print_board(board)
        if solve_sudoku(board):
            print("\nSolved Sudoku:")
            print_board(board)
        else:
            print("\nNo solution exists for the given Sudoku board.")
    else:
        print("\nThe Sudoku board is not valid.")

if __name__ == "__main__":
    main()
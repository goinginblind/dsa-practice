
def isValidSudoku(board: list[list[str]]) -> bool:
    row_set = set()
    column_set = set()
    box_set = set()
    for row_index, row in enumerate(board):
        for column_index, symbol in enumerate(row):
            if symbol.isdigit():
                if (row_index, symbol) not in row_set and \
                      (column_index, symbol) not in column_set and \
                          (row_index // 3, column_index // 3, symbol) not in box_set:
                    row_set.add((row_index, symbol))
                    column_set.add((column_index, symbol))
                    box_set.add((row_index // 3, column_index // 3, symbol))
                else:
                    return False
    return True


def main():
    board = [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","1",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))    

main()   
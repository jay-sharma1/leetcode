def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        if not noDuplicatesRow(row):
            return False

    for ind in range(0, 9):
        if not noDuplicatesColumn(board, ind):
            return False
    
    for ind1 in range(0, 7, 3):
        for ind2 in range(0, 7, 3):
            if not noDuplicatesSquare(board, [ind1, ind2]):
                return False
    
    return True
        

def noDuplicatesRow(row: list[str]) -> bool:
    rowSet = set()
    for elem in row:
        if elem != ".":
            if elem in rowSet:
                return False
            else:
                rowSet.add(elem)

    return True
    
def noDuplicatesColumn(board: list[list[str]], columnNum: int) -> bool:
    # Given a board and the column you wish to check, determines if that column has any duplicates
    columnSet = set()
    
    for row in board:
        box = row[columnNum]
        
        if box != ".":
            if box in columnSet:
                return False
            else:
                columnSet.add(box)
    
    return True

def noDuplicatesSquare(board: list[list[str]], corner: list[int]) -> bool:
    currentSet = set()

    for ind1 in range(corner[0], corner[0] + 3):
        for ind2 in range(corner[1], corner[1] + 3):
            # Iterates through all 9 boxes within the square denoted by the original top left corner
            box = board[ind1][ind2]
            
            if box != ".":
                if box in currentSet:
                    return False
                else:
                    currentSet.add(box) 
                    
    return True

# Test

board1 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board1))
print(isValidSudoku(board2))
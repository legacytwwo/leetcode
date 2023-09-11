def isValidSudoku(board: list[list[str]]) -> bool:
    rows = {i:set() for i in range(9)}
    columns = {i:set() for i in range(9)}
    boxes = {(i, j): set() for i in range(3) for j in range(3)}

    for row in range(len(board)):
        for column in range(len(board[row])):
            number = board[row][column]
            if number == '.':
                continue
            box_index = (row // 3, column // 3)
            if (number not in rows[row]) and (number not in columns[column]) and (number not in boxes[box_index]):
                boxes[box_index].add(number)
                rows[row].add(number)
                columns[column].add(number)
            else:
                return False
    return True


assert isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
) == True
assert isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
) == False
assert isValidSudoku(
    [[".",".",".",".","5",".",".","1","."]
    ,[".","4",".","3",".",".",".",".","."]
    ,[".",".",".",".",".","3",".",".","1"]
    ,["8",".",".",".",".",".",".","2","."]
    ,[".",".","2",".","7",".",".",".","."]
    ,[".","1","5",".",".",".",".",".","."]
    ,[".",".",".",".",".","2",".",".","."]
    ,[".","2",".","9",".",".",".",".","."]
    ,[".",".","4",".",".",".",".",".","."]]
) == False
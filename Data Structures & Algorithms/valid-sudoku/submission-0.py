class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            numSet = set()
            for col in row:
                if col in "123456789" and col in numSet:
                    print("row")
                    return False
                else: 
                    numSet.add(col)

        # check col
        for col in zip(*board):
            numSet = set()
            for row in col:
                if row in "123456789" and row in numSet:
                    print("col")
                    return False
                else:
                    numSet.add(row)

        # check box
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = (i//3, j//3)
                if board[i][j] in "123456789" and board[i][j] in boxes[curr]:
                    print("box")
                    return False
                else:
                    boxes[curr].add(board[i][j])

        return True
            


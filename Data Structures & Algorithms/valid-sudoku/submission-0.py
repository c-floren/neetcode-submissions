from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force: o(n^2)
        # double forloop

        # understanding the problem:
        # only filled in cells matter
        # ignore empty positions
        # approach:
        # hash set for each row in the grid
        # hash set for each col in the grid
        # hash set for each box in the grid
        # index for a 3x3 box is i // 3
        # key (r//3, c//3)

        # time: O(n^2)
        # space: O(n^2)

        # checking for duplicates
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r//2, c//3)

        for r in range(9):
            for c in range(9):
                # if empty spot
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        # didn't detect any duplicates
        return True


        
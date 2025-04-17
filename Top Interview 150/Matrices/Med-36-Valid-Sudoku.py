class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        we need to check
        1. Horizontal
        2. Vertical
        3. 3x3 square
        """
        import collections

        rows_seen = {i: set() for i in range(len(board))}
        cols_seen = {i: set() for i in range(len(board))}
        square_seen = collections.defaultdict(set)

        # First pass - horizontal and vert

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_seen[r] 
                    or board[r][c] in cols_seen[c] 
                    or board[r][c] in square_seen[(r // 3, c // 3)]):
                    return False
                else:
                    cols_seen[c].add(board[r][c])
                    rows_seen[r].add(board[r][c])
                    square_seen[(r // 3, c // 3)].add(board[r][c])
        return True
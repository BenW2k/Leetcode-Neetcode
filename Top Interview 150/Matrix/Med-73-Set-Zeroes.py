class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # For the O(1) space solution we can traverse through in the m*n time
        # if there is a 0 then we set the left most val in the row to 0 and the top most val in the col to 0
        # (we've already visited both)
        # we need a single extra variable to avoid the overlapping of row and col nums at  the origin (0,0)
        
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        # detemine which rows and cols need to be 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True


        # We skip the first row and col for now to avoid changing our pointers (the first cols)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
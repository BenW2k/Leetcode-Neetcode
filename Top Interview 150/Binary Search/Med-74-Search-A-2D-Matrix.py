class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1
            if matrix[i][0] > target:
                return False
            if matrix[i][0] == target:
                return True
            while l <= r:
                mid = (l + r) // 2
                if target > matrix[i][r]:
                    break
                if target > matrix[i][mid]:
                    l = mid + 1
                elif target < matrix[i][mid]:
                    r = mid - 1
                else:
                    return True
        return False
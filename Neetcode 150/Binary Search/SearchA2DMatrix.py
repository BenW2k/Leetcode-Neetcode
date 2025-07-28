class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml = 0
        mr = len(matrix) - 1
        while ml <= mr:
            mid = ml + ((mr - ml) // 2)
            l = 0
            r = len(matrix[mid]) - 1

            if (target > matrix[mid][l]) and (target > matrix[mid][r]):
                ml = mid + 1
            elif (target < matrix[mid][l]) and (target < matrix[mid][r]):
                mr = mid - 1
            else:
                while l <= r:
                    new_mid = l + ((r - l) // 2)
                    if target > matrix[mid][new_mid]:
                        l = new_mid + 1
                    elif target < matrix[mid][new_mid]:
                        r = new_mid - 1
                    else:
                        return True
                return False
        return False
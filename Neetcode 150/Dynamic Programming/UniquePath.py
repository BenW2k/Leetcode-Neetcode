class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution 2: Top-down DP (Memoization)
        # Time: O(m*n)
        # Space: O(m*n)

        memo = {(0,0): 1} # We add our base case to the memoization hashmap

        # We create the recursive helper function
        def paths(i, j):
            if (i, j) in memo: # Looks in the hashmap at O(1) and avoids calculating it again
                return memo[(i,j)]
            elif i < 0 or j < 0 or i == m or j == n: # This is setting the out of bound locations to 0
                return 0
            else:
                val = paths(i, j - 1) + paths(i-1, j) # To get the val this is adding up the number of paths we get from the left and the number of paths we get from above
                memo[(i, j)] = val # We add the new (i, j) val to the memo the first time we see it so we dont have to compute it again
                return val
        
        return paths(m-1, n-1)
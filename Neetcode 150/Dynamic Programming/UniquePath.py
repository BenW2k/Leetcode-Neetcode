class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Solution 1 - Recursive Brute Force
        # Time: O(2^(m*n)) - Because if it takes (m-1) + (n-1) to reach the bottom right corner and you have 2 choices at each square (either right or down) then it will be 2^(m*n)
        # Space: O(m*n) - because of the recursive call stack

        def paths(i, j):
            if i == j == 0: # Base case: if we're at the origin there is 1 way to get there
                return 1
            elif i < 0 or j < 0 or i == m or j == n: # If we're out of bounds, return 0
                return 0
            else:
                return paths(i, j - 1) + paths(i - 1, j) # We get the ways to get to this position by adding the num of ways from the left and the num of ways from the top
            # We don't store any of the results so we have to calculate the entire recursive call stack each time.
        
        return paths(m-1, n-1) # return the main result, it will work out all sub problems.



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


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Solution 3: Bottom UP DP (Tabulation)
        # Time O(m*n)
        # Space O(m*n)

        dp = [] # Initialising the tabulation array

        # This adds m lists to the dp array each with n 0s inside
        
        for _ in range(m): # we use a placeholder val for i as we're not referencing it in the code block
            dp.append([0] * n) # we create an array the length of m filled with placeholder 0s
        
        dp[0][0] = 1 # We set the origin to 1 as our base case

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue # We don't build up the grid for the first position so it stays as 1
                
                val = 0
                if i > 0: # This is to ensure that if we're on the top row we don't want to add anything from above
                    val += dp[i-1][j]
                if j > 0: # This is to ensure that if we're on the leftmost column, we don't want to add anything from the left
                    val += dp[i][j - 1]
                
                dp[i][j] = val

        return dp[m-1][n-1]


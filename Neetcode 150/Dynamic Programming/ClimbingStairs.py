class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution: # Fibonacci Sequence
    def climbStairs(self, n: int) -> int:
        j = 0
        k = 1
        total = 1
        for i in range(n - 1):
            j = k
            k = total
            total = j + k
        return total
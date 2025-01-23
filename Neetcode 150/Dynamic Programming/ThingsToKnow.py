# The approaches to dynamic programming

# 1. Naive Recursion - sub-optimal method usually accompanied by a very large run time like O(2^n) or O(n!)


# 2. Top-down Dynamic Programming - Memoization (Recursive)


# 3. Bottom-up Dynamic Programming - Tabulation (Loops) - usually faster given their greater efficiency than recursion


# 4. If Possible - O(1) space Bottom-up DP

# Small example of leetcode easy fib numbers

# Approach 1 - Memoization O(n) time O(n) space


class Solution(object):
    def fib(self, n):

        memo = {0:0, 1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
            
        return f(n)
        
        


# Approach 2 - Tabulation O(n) time O(1) space


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n  == 0:
            return 0
        j = 0
        k = 1
        target = 1

        for i in range(1, n):
            target = j + k
            j = k
            k = target
        
        return target
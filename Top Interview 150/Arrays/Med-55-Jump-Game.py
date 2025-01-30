class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Recursive solution, Time: O(max(nums)^n), Space: O(n)
        # not optimal and won't pass the test cases due to time

        n = len(nums)

        def can_reach(i):
            if i == n - 1: # if we're at the last index of the list
                return True

            for jump in range(1, nums[i] + 1):
                if can_reach(i+jump):
                    return True
            
            return False

        return can_reach(0)
    
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Top Down Memoization DP solution
        # Time: O(n^2)
        # Space: O(n)

        n = len(nums)
        memo = {n-1 : True}


        def can_reach(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):
                if can_reach(i+jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return can_reach(0)
    
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Optimal solution - Greedy sort, starting at the end
        # Time O(n)
        # Space O(1)

        n = len(nums)
        target = n - 1 # starting our target at the last index
        for i in range(n-1, -1, -1): # We're going backwards starting at N-1 inclusive and decrementing until -1 exclusive (so we're actually going down until 0)
                                    # and decrementing the index by 1 every time
            max_jump = nums[i] # this is the max we can jump at a given index
            if i + max_jump >= target: #if we can get to the target from our ith position then we set that as the new target
                target = i
        
        return target == 0
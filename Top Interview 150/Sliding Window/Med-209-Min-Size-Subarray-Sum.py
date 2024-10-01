class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        current_sum = 0
        min_sum = len(nums) + 1
        
        for r in range(len(nums)):
            current_sum += nums[r]
            if min_sum == 1:
                return min_sum
            while current_sum >= target:  
                min_sum = min(r-l + 1, min_sum)
                current_sum -= nums[l]
                l += 1
        if min_sum < len(nums) + 1:
            return min_sum
        else:
            return 0  
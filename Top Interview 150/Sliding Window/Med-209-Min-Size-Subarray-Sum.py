class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #Prerequisites
        # Only positive numbers, max O(n), return 0 if no such subarray, returning minimal length
        l = 0 # initialise left pointer
        current_sum = 0 # initialise the current sum of all elements in the sliding window
        min_sum = len(nums) + 1 # create a placeholder value out of bounds for the array so we know that if we are left with this at the end of the loop
        # then we know that there is no such subarray and can return 0
        
        for r in range(len(nums)): # using r as the index for the for loop and the right pointer
            current_sum += nums[r] # we add nums[r] to the current sum with every iteration
            if min_sum == 1: # 1 is the minimum possible value given that target cannot be <= 0. So terminate the loop early if we find a subarray of size 1
                return min_sum
            while current_sum >= target:
                min_sum = min(r-l + 1, min_sum) #min sum is equalled to the smaller number of r - l + 1 (which is how you calculate the length of the sliding window) and the current min sum
                current_sum -= nums[l] # subtract nums[l] from the current sum and move l one place up the array
                l += 1
        if min_sum < len(nums) + 1: #final check to see if there has been a valid subarray found
            return min_sum
        else:
            return 0  
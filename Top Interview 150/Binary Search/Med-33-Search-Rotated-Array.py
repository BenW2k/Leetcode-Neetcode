class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Prerequisites:
        # O(logn) - binary search
        # distinct values
        # 0 indexed.
        # All values of nums are unique
        # ascending array possibly rotated
        # Possibly rotated - meaning not always
        # return index of target or -1 after rotation
        # potential edge case: all elements are still in order, element not in nums,

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: # if m is the target return it
                return m
            # left sorted portion
            if nums[l] <= nums[m]: # if nums l is less than nums m it means we're in the left sorted portion
                if target > nums[m] or target < nums[l]: # if the target is greater than m or less than l then it means we need to swap to the right sorted portion
                    l = m + 1
                else:
                    r = m - 1 # else continue with left side

            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]: # if m is greater or r is less than it means we're in the wrong sorted portion and need to move to the other
                    r = m - 1
                else: # else continue as normal in the right side of the array
                    l = m + 1
        return -1 # return -1 if we don't see the target in there

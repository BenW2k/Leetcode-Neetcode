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
            if target == nums[m]:
                return m
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r= m - 1
                else:
                    l = m + 1
        return -1

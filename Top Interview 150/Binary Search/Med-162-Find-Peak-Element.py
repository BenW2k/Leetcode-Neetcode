class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #prequisities:
        # Any two neighbouring elements are not equal
        # Any element outside of the array is less than its neighbour inside the array
        # O(logn) - alluding to binary search
        # If there are multiple peaks return the index of any peak

        # Basically we know which way to search with the binary search because:
        # 1. If the right element is greater than mid then we can assume there will be a maximum that side of the array
        # (this is due to the fact that if the furthest right point nums[i] is greater than nums[i-1] then it is a maximum due to it being larger
        # than its neighbouring value outside of the array by default)
        # 2. Same goes for the left side
        # 3. If both points are smaller than the mid point then the mid point is a peak element and is returned.

        l = 0 # initialise left pointer at start of array
        r = len(nums) - 1 # initialise right pointer at end of array

        while l <= r: # ensures pointers don't cross over
            m = ((l + r) // 2) # creates the midpoint
            if m > 0 and nums[m] < nums[m - 1]: # m > 0 is to deal with the edge case at the left side of the array
                r = m - 1 # makes the right pointer the mid to only search the left side of the array
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]: # m < len(nums) - 1 is for the edge case at the right side of the array
                l = m + 1 # makes the left pointer the mid to only search the right side of the array
            else:
                return m  # returns m as peak
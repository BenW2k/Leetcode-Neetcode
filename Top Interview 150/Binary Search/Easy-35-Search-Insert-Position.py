class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # If the target element is not in the array then return the index where it would be if it were.
        # This is a binary search solution

        l = 0 # initialises left pointer at start of array
        r = len(nums) - 1 # initialises right pointer at end of array

        while l <= r: #
            mid = (l + r) // 2 # finds the middle element of the array
            if nums[mid] > target: # if it is larger than the target then we disregard the numbers larger than it and set the right pointer to the start of the list minus 1 
            # (because we just checked mid and know it isn't that)
                r = mid - 1
            elif nums[mid] < target: # If its smaller we disregard the numbers smaller than it and set the left pointer to the middle.
                l = mid + 1
            else:
                return mid # If it is in the list then we just return mid (as it is asking for the index of target not the actual target number)
        return l # If it isn't in the array we return the left-most pointer. 
        # This is because of a case where there is one element left in the search. If the target is less than the element then the right pointer
        # will move to the left and this will give the wrong index, the left pointer stays in place (the index of where the element would actually be placed)
        # If the target is greater than the element then the left pointer will move to the right and will be in the correct index for an element larger than the remaining element.
        # This could also be achieved by just doing a check at the end where if mid is greater than target its index is mid+1 else its just mid.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # essentially the code goes through the array and removes any element that is equal to our target val and increments the counter
        # returns the finished array
        i = 0 # initialises counter
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
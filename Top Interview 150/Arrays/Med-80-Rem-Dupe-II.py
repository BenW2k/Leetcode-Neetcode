class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Prerequisites:
        # O(1) additional memory which means I can't create a hashmap for comparison.
        # Two point doesn't create additional memory
        # return k where k is the num of valid nums in nums
        # Array is pre-sorted
        # Final array isn't allowed more than 2 instances of same num

        # pointer for checking the ith term and another pointer to check 2 indexes ahead to see if its the same (array is sorted so if its the same its a guaranteed >2 dupe)
        i = 0
        j = 2
        
        while j <= len(nums) - 1:
            if nums[i] == nums[j]: #checks if nums are the same and deletes if so because guaranteed to be >2 dupe
                del nums[j] # doesn't increment because removing element means j will be a new element and needs to be checked for a dupe.
            else: #increments as usual
                i += 1
                j += 1
        
                    
        return len(nums) #returns k where k is the count of passing nums in the array.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Things to note:
        # return k where k= num of unique ints in list
        # remove duplicates in place
        # return nums (meaning you can't return a fresh list)


        map = {} # Instantiating hashmap (dict)
        i = 0 # counter for loop

        while i <= len(nums) - 1: #loops while i is in range of the loop
            if nums[i] not in map: # Checks if current num is already in map (if so its a duplicate)
                map[nums[i]] = nums[i] #if not it adds it
                i += 1 # increments count

            else: #else it deletes nums[i] and doesn't increment i because nums[i] is now the next num in the list
                del nums[i]
        return len(nums) # returns k

class Alt_Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1 #counter
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: # List is ordered so you can compare nums[i] to previous index to see if its a duplicate.
                nums[j] = nums[i]
                j += 1
        return j
        
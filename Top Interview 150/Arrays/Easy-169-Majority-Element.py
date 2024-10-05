class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My first, slightly convoluted solution, O(n) both mem and time comp
        # Basically adds all numbers to a map and counts the times they occur in the array
        # As only one majority element exists, it returns the element that's count is greater than half the size of the array.
        map = {}
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
                if map[nums[i]] > (len(nums) / 2):
                    return nums[i]
                

# Alt more simplistic solution
# Just sorts the array and returns the number thats at the middle of the array (will always be the majority element)
# Python's sort func is O(nLogn) and the mem comp is O(1) additional mem

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        return nums[len(nums) // 2]
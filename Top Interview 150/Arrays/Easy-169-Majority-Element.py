class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
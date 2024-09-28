class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # this question states that it is a one-indexed array meaning it starts at 1
        i = 0 # first pointer (still 0 because loops still operate at 0 regardless)
        j = len(numbers) - 1 # right pointer

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1] # adding 1 to each element in the return list because its one indexed
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1    
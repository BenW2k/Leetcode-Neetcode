class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0: # if the array is empty return 0
            return 0
        i = 0 # sets the first pointer to the start of the index
        j = len(height) - 1 # sets last pointer to the end of the index
        curr_max = 0 # var for current max of the containers

        while i < j: # while the pointers dont cross
            diff = j - i # this is to find the length of the container
            n = (diff * min(height[i], height[j])) # this is to find the height, no skew so you take the minimum of both values

            if curr_max < n :
                curr_max = n
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return curr_max
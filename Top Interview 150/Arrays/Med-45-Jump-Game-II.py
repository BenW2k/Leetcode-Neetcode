class Solution:
    def jump(self, nums: List[int]) -> int:
        # An element of greedy, using a sort of sliding window technique
        # Time: O(n)
        # Space: O(1)

        res = 0 # creating our result integer
        l = r = 0 # creating our window pointers
        
        while r < len(nums) - 1: # while our rightmost pointer is not at the last index in the array (that would be the final solution)
            farthest = 0 # initialise the farthest variable
            for i in range(l, r + 1): # searches the window as r + 1 is exclusive.
                farthest = max(farthest, i + nums[i]) # if farthest is beaten the higher number becomes the new farthest
            l = r + 1 # after that loop we set l to be the start of a new window at the index beyond the rightmost index
            r = farthest # we set r as the farthest we've gotten so far
            res += 1 # We increment the result by 1 indicating an additional minimum step
        return res
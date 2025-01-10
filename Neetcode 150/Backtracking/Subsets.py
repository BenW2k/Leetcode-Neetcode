class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n: # this is how we know we're at a leaf node
                res.append(sol[:]) # we append the sol[:] instead of just sol because sol is a reference to the sol object whereas sol[:] is a copy of the sol list
                return
            
            #Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        
        backtrack(0) # this starts the backtracking function at 0
        return res
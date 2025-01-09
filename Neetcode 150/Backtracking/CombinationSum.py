class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], [] # initialise our results and solution lists

        def backtrack(i):
            if sum(sol) == target: # no duplicate lists so if the sum of sol is equal to target and solution isn't already in res list we append a copy of sol
                if sol not in res:
                    res.append(sol[:]) # this copy of sol is important because of we did sol instead then we're copying a reference to the object rather than cloning the list
                return
            if i == len(nums): # return if we reach end of list
                return
            
            if sum(sol) > target: # no negative numbers so if we go over the target we can just return
                return
            
            # we don't take

            backtrack(i+1)

            # we take the same num again

            sol.append(nums[i])
            backtrack(i)
            sol.pop()


            # we take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res
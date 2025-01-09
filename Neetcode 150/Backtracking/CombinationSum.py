class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            if sum(sol) == target:
                if sol not in res:
                    res.append(sol[:])
                return
            if i == len(nums):
                return
            # we don't take

            if sum(sol) > target:
                return
            backtrack(i+1)

            # we take the same num again
            sol.append(nums[i])
            backtrack(i)
            sol.pop()


            # we take current

            # we take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res
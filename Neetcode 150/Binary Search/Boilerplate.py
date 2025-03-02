# Traditional Binary Search O(logn) O(1) space
def trad_binary(nums, target):

    n = len(nums)
    L = 0
    R = n - 1

    while L <= R:
        M = L + ((R-L) // 2)

        if nums[M] == target:
            return True
        elif target < nums[M]:
            R = M - 1
        else:
            L = M + 1

    
    return False

# Condition-based Binary Search

def condition_binary(nums):
    n = len(nums)
    l = 0
    r = n - 1

    while l < r: # has to be less than r to force it to escape at some point. Particularly when they're equaL to each other.
        M = l + ((r-l) // 2)


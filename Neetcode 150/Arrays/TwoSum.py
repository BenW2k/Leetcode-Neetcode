def twoSum(nums, target):
    map = {}
    for i, n in enumerate(nums):
        res = target - n
        if res in map:
            return [i, map[res]]
        map[n] = i
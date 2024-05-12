def twoSum(nums, target):
    map = {} # Initialises empty hashmap
    for i, n in enumerate(nums): # where i is the index and n is the value at that index.
        res = target - n # The number we're looking for is the result of the sum target - n
        if res in map: # if the result of this sum is already in our map
            return [i, map[res]] # return list object [index of current, index of target-n] because question is looking for indexes not values.
        map[n] = i # if res isn't in map, add the current iteration values to the map where the key is the value in nums and i is the value.
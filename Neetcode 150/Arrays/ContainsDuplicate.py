def containsDuplicate(nums):
    check = {}
    for i in range(len(nums)):
        if nums[i] in check:
            return True
        else:
            check[nums[i]] = i
    return False
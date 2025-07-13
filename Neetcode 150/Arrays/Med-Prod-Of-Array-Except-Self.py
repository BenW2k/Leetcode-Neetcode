class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        print(product)
        if zero_count > 1:
            return [0] * len(nums)
        else:
            product_list = [product] * len(nums)
        if zero_count == 1:
            for i in range(len(product_list)):
                if nums[i] == 0:
                    product_list[i] = product
                else:
                    product_list[i] = 0
        else:
            for i in range(len(product_list)):
                if nums[i] == 0:
                    product_list[i] = product
                else:
                    product_list[i] = product_list[i] // nums[i]
        
        return product_list


# 2nd solution - O(n) time complexity, O(1) space complexity (as stated return array doesn't count) prefix and postfix method (no division)
# so you want to find the product of all numbers to the left (prefix) and right (postfix) of the current index
# We pass twice through the array, the first time we find the prefix and store it in the result array
# the second time we find the postfix and multiply it with the prefix we found in the first pass
# this way we don't need to use division and we can find the product of all numbers to the left and right of the current index


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
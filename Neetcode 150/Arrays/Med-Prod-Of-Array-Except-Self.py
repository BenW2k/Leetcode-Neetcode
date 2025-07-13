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

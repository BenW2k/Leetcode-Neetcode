def threeSum(nums):
    mylist = []
    nums.sort()
    i = 0
    j = 1
    k = len(nums) - 1
    for i in range(len(nums)):
        j= i + 1
        print(f'{nums[i]} + {nums[j]} + {nums[k]}')
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                print(f' test {i} j = {j} k = {k}')
                res = [nums[i], nums[j], nums[k]]
                print(res)
                if res not in mylist:
                    mylist.append(res)
                    print(mylist)
                j+=1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -=1
            else:
                j+=1
    return mylist

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
desired = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

threeSum(nums)
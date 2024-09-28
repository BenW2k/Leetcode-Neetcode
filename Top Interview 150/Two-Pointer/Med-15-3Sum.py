class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        prerequisites:
        two pointer: solution sets must not contain dupe sets
        likely a process where dupes are not even checked.
        """

        # This first solution isn't the most efficient due to the fact that we are checking through the array every time we need add an element
        # and our least likely condition is first so it is unlikely that we break the if statements on the first clause leading to extra computation.
    
        output = [] # Returns the output array of arrays
        nums.sort() #Sorts input array
        
        for i in range(len(nums) - 2): #loops through the element but stops at 2nd last because we have 3 pointers and therefore need 3 unique numbers to continue.
            j = i + 1 # i is always the first pointer, j the middle
            k = len(nums) - 1 #k, the last pointer
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0: #if it satisfies our target conditions
                    if [nums[i], nums[j], nums[k]] not in output: #check if the result already isn't in the array
                        output.append([nums[i], nums[j], nums[k]]) #if not, append it
                    k -= 1 #then move the 2 pointers so they're not on the same numbers.
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    j += 1
        return output

class 2ndSolution(object):
    def threeSumBetter(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        prerequisites:
        two pointer: solution sets must not contain dupe sets
        likely a process where dupes are not even checked.
        """
        # O(n^2) solution but increased efficiency compared to the solution above
        output = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: #first checks if i isn't the first element (otherwise looking for i-1 will return index error)
                continue # Then continues if nums[i] is the same as the element before it, because if so, the only potential solution would be a duplicate anyway.
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k]) > 0: # checks the other likely conditions first.
                    k -= 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]]) # appends, we know it wont be a duplicate because we've caught them already above.
                    j += 1
                    while nums[j] == nums[j-1] and j < k: # this is a similar concept to the check at the start of the for loop, basically moving across the pointer j
                        j += 1 # until it is a unique number to avoid looping through duplicates.
        return output

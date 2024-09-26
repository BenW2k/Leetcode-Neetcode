class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Notes:
        # Unable to create a new array with just the objects we need due to the constraint of having to return the original nums1 array.
        # Given that there is already space in nums1 for the merge, we can assume that we are able to compare the arrays in order to sort them in non-decreasing order.
        # The empty space is at the end of nums1 which leads us to start merging and comparing from the end of nums1
        # Potential edge cases: n or m <= 0, m reaches 0 whilst n > 0 leaving leftover nums in nums2 to be sorted.

        # Create last index to traverse through nums1 (-1 due to it being used as an index and array indexing starts at  )
        last = m + n - 1

        # Merging in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]: # Comparing numbers to see which is larger
                nums1[last] = nums1[m] # setting the number at the last pointer to nums1[m]
                m -= 1 # moving the pointer in nums1 down
            else: #If the numbers are equal or nums2[n - 1] is larger we can set last to nums2[n-1] and decrement n
                nums1[last] = nums2[n]
                n -= 1
            last -= 1 # decrement last at end of each iteration.
        
        # Fill nums1 with the leftover elements from nums2 in the event we reach the end of nums1 and n is still greater than 0
        while n > 0:
            nums1[last] = nums2[n]
            n, last = n - 1, last - 1 #interesting comprehension.

    def alt_solution(self, nums1, m, nums2, n):

        end = m + n - 1 # Creates end point

        for i in range(n): # Iterates over the length of nums2
            nums1[end] = nums2[n - 1]
            end -= 1
            n -= 1
        nums1.sort() # sorts after replacing all of the 0's with nums2 numbers. (because native functions are likely more efficient than making you're own lol)
    
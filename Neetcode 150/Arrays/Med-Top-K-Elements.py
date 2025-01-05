class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      # Basically you want to add each number to a hashmap with the amount of times they occur in the array
      # You want to destructure the key-value pairs from the dict and store an array of numbers that occur the amount of times that they're at in the index
      # e.g all elements that occur twice are at the freq[2]
      # then you want to initialise another array and iterate from the end of the frequency array, iterating through its subarrays adding numbers
      # from largest first until there are k elements in the result array (len(res) == k)
      # then just return res
        map = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            map[nums[i]] += 1
        
        for n, c in map.items():
            freq[c].append(n)
        
        res = []
        j = len(freq) - 1
        while j > 0:
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res
            j -= 1
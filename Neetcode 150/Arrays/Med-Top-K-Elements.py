class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
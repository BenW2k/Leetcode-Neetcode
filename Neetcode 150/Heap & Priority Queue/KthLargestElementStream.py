import heapq

class KthLargest:
    # The quirk in this one was that you're allowed to only keep the elements you want
    # so by maintaining a heap the size of k we can effectively call heap[0] for the kth largest element in the heap
    # we are using a min heap here with time complexity of O(mlogk) where m is the number of add() calls and k is the rank of largest number to be tracked
    # space complexity is O(k)

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k: # makes the heap k size
            heapq.heappop(nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, (val))
        if len(self.nums) > self.k: # this is for an edge case where the list starts with less than k elements, so it avoids keeping the list below k elements long
            heapq.heappop(self.nums)

        return self.nums[0]
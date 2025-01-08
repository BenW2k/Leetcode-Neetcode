import heapq
class Solution:
    # creates a max heap by negating values then heapify, pops k-1 elements, then returns the next pop which will be the kth largest (* by -1 to revert negation)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        for _ in range(k -1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

class Solution:
    # creates a min heap of k size then at the end of the loop it returns the first element in the list which should be the kth largest element in the array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]

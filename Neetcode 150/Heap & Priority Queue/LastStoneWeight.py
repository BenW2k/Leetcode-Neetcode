class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # invert positive and negative integers to make max heap

        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, (x - y))
            elif y < x:
                heapq.heappush(stones, (y - x))
            heapq.heapify(stones)
        
        if stones:
            return (stones[0] * -1)
        else:
            return 0
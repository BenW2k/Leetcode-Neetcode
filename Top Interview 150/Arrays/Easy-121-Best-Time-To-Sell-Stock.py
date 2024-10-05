class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        output = 0

        while j < len(prices):
            if prices[i] < prices[j] :
                output = max(output, prices[j] - prices[i])
            else:
                i = j
                
            j += 1
        return output
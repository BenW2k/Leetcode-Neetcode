class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # This question only permits us to buy and sell once, as opposed to multiple times like its medium counterpart
        # i needs to be smaller than j to sell at profit.
        # if the earlier value is more than the right value, the left pointer moves to the position of the right
        # right pointer moves with every iteration.
        # output is the max between the current recorded output and the output of the current iteration.
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
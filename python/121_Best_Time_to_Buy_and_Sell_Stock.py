class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
    
        min_price = prices[0]
        profit = 0

        for p in prices[1:]:
            profit = max(profit, p - min_price)
            min_price = min(min_price, p)
        return profit
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        free = 0
        have = cool = -float('inf')
        
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
            
        return max(free, cool)
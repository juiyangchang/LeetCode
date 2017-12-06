import math
class Solution:
    cache = {0: 0}
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n in self.cache:
                return self.cache[n]
            
            ans = float('inf')
            for i in range(int(math.sqrt(n)), 0, -1):
                new_ans = helper(n - i**2)
                if new_ans + 1 < ans:
                    ans = new_ans + 1
            self.cache[n] = ans
            return ans         
        
        if n in self.cache:
            return self.cache[n]
        
        ans = helper(n)
        return ans                
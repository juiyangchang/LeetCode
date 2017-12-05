class Solution:
    cache = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache: 
            return self.cache[n]
        
        if n < 2:
            self.cache[n] = 1
            return 1
        else:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.cache[n]
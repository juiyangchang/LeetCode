class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {1:1}

        def helper(n, n_split = 0):
            if n in cache:
                return cache[n]
            
            ans = n if n_split != 0 else 0
            for i in range(n-1, 0, -1):
                tmp = i * helper(n-i, n_split+1)
                if tmp > ans:
                    ans = tmp
            cache[n] = ans
            return cache[n]
        
        if not n:
            return 0
        else:
            return helper(n)
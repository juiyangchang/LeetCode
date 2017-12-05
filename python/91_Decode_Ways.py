class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [1] + [0] * len(s)
        
        dp[1] = dp[0] if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] = dp[i]
            
            if s[i-1:i+1] > '09' and s[i-1:i+1] < '27':
                dp[i+1] += dp[i-1]
                
        return dp[-1]
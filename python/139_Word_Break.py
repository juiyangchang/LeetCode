class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                len_w = len(w)
                if i+1 >= len_w and s[i-len_w+1:i+1] == w and dp[i+1-len_w]:
                    dp[i+1] = True
        return dp[-1]
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        head = -1
        last_seen = {}
        
        for idx, c in enumerate(s):
            if c in last_seen and head < last_seen[c]:
                head = last_seen[c]
                
            if ans < idx - head:
                ans = idx - head
                
            last_seen[c] = idx
            
        return ans
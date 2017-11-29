from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        seen = defaultdict(int)
        
        for i in range(len(s)-9):
            seen[s[i:i+10]] += 1            
            
        return [s for s, count in seen.items() if count > 1]
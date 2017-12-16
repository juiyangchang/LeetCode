import string
from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0        
        
        count = defaultdict(int)
        lookup = 'z' + string.ascii_lowercase
        max_len = 1
        count[p[0]] = 1
        
        for i, c in enumerate(p[1:]):
            if ord(c) - ord(p[i]) == 1 or ord(c) - ord(p[i]) == -25:
                max_len += 1
            else:
                max_len = 1
        
            if count[c] < max_len:
                count[c] = max_len
                
        return sum(count.values())
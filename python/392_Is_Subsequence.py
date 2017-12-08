from collections import defaultdict
from bisect import bisect
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def create_map(seq):
            pos_tbl = defaultdict(list)
            for i, c in enumerate(seq):
                pos_tbl[c].append(i)
            return pos_tbl
        
        pos_tbl = create_map(t)
        # position in t of the last seen character from s
        last_pos = -1
        
        for c in s:
            if c in pos_tbl:
                pos_list = pos_tbl[c]
                idx = bisect(pos_list, last_pos)
                if idx == len(pos_list):
                    return False
                else:
                    last_pos = pos_list[idx]
            else:
                return False                
        return True         
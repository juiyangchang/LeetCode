from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)
            
        return list(res.values())
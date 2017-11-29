class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        lookup = {}
        t_set = set([])
        
        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])
            
            if (s[i] in lookup and diff != lookup[s[i]]) \
                or (s[i] not in lookup and t[i] in t_set):
                return False
            
            lookup[s[i]] = diff
            t_set.add(t[i])
                
        return True
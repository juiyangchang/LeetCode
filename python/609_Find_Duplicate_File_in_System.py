from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        lookup_tbl = defaultdict(list)
        
        for p in paths:
            files = p.split()
            root, files = files[0], files[1:]
            for f in files:
                fname, content = f.split('(')
                lookup_tbl[content[:-1]].append(root + '/' + fname)
                
        return list(filter(lambda x: len(x) > 1, lookup_tbl.values()))
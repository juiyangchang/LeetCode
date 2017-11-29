from collections import defaultdict
from itertools import accumulate

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        count = defaultdict(int)
        
        for idx, row in enumerate(wall):
            for acc in accumulate(row):
                count[acc] += 1      
        
        if len(count) == 1:
            return len(wall)
        else:
            count[acc] = -1
            return len(wall) - max(count.values())
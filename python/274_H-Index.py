class Solution:
    '''
    https://discuss.leetcode.com/topic/40765/java-bucket-sort-o-n-solution-with-detail-explanation/2
    '''
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        bucket = [0] * (len(citations) + 1)
        for c in citations:
            if c >= len(bucket):
                bucket[-1] += 1
            else:
                bucket[c] += 1
            
        count = 0
        for i in range(len(citations), -1, -1):
            count += bucket[i]
            if count >= i:
                return i
        return 0
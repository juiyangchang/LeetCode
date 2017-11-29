class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        cnt = ans = 0
        lookup = {0: -1}
        
        for idx, n in enumerate(nums):
            cnt += (2*n - 1)
            if cnt in lookup:
                length = idx - lookup[cnt]
                if ans < length:
                    ans = length
            else:
                lookup[cnt] = idx
            
        return ans
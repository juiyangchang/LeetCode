class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        e = i = 0
        for n in nums:
            tmp = i
            i = e + n
            e = max(tmp, e)
        return max(i, e)
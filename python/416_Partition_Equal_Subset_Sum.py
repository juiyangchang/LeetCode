class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(remain, start, end, cache):
            if remain in cache:
                return cache[remain]
            
            if remain == 0:
                return True
            
            cache[remain] = False
            if remain > 0:
                if any(helper(remain - nums[i], i+1, end, cache) for i in range(start, end)):
                    cache[remain] = True
            
            return cache[remain]
        
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        return helper(tot // 2, 0, len(nums), {})
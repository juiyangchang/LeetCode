class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums):
            if not nums:
                return 0
            e = i = 0
            for n in nums:
                tmp = i
                i = e + n
                e = max(tmp, e)
            return max(e, i)
        
        if not nums:
            return 0        
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(helper(nums[:-1]), helper(nums[1:]))
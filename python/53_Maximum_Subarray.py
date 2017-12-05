from itertools import accumulate
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_sum, ans = 0, -float('inf')
        for running_sum in accumulate(nums):
            ans = max(ans, running_sum - min_sum)
            min_sum = min(min_sum, running_sum)
        return ans
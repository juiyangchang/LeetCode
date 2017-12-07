from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        for n in nums:
            idx = bisect_left(tails, n)
            if idx >= len(tails):
                tails.append(n)
            else:
                tails[idx] = n
        return len(tails)
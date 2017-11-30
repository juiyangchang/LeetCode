from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ctr = Counter(nums)
        nums = [no for no in range(1, len(nums)+1) if ctr[no] != 1]
        return nums if ctr[nums[0]] == 2 else nums[::-1]
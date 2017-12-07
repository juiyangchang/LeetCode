class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums.sort()
        end_idx = 0
        pre_idx = [-1] * len(nums)
        set_len = [1] * len(nums)
        max_len = 1
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    count = set_len[j] + 1
                    if count > set_len[i]:
                        set_len[i] = count
                        pre_idx[i] = j
            if set_len[i] > max_len:
                max_len = set_len[i]
                end_idx = i
    
        res = []
        while end_idx != -1:
            res.append(nums[end_idx])
            end_idx = pre_idx[end_idx]
        return res[::-1]
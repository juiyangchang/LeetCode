class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def helper(k, target, current, start):
            if k == 1:
                    return True
            if current == target:
                return helper(k-1, target, 0, 0)
            
            for i in range(start, len(nums)):
                if not visited[i] and nums[i] + current <= target:
                    visited[i] = True      
                    if helper(k, target, current+nums[i], i+1):
                        return True
                    visited[i] = False         
            return False        
        
        if k == 1:
            return True
        if len(nums) < k:
            return False
        tot = sum(nums)
        if tot % k != 0:
            return False
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        return helper(k, tot // k, 0, 0)      
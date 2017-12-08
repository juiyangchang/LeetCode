from collections import defaultdict
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        combinations = defaultdict(int)
        combinations[0] = 1
        nums.sort()
        
        for i in range(nums[0], target+1):
            for e in nums:
                if i - e in combinations:
                    combinations[i] += combinations[i-e]
                elif i - e < 0:
                    break
                    
        return combinations[target]
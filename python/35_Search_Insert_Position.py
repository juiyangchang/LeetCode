class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            m_val = nums[mid]
            
            if m_val < target:
                left = mid + 1
            else:
                right = mid
                
        return left+1 if nums[left] < target else left
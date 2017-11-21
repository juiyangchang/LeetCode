class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            m_val = nums[mid]
            
            if m_val < target:
                left = mid + 1
            else:
                right = mid
                                                
        if nums[left] != target:
            return [-1, -1]
        else:
            l_bnd = left
            
            left, right = 0, len(nums) - 1
            
            while left < right + 1:
                mid = left + (right - left) // 2
                m_val = nums[mid]
                
                if m_val > target:
                    right = mid - 1
                else:
                    left = mid + 1
                                        
            return [l_bnd, right]
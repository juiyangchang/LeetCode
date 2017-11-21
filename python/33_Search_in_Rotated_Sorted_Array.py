class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left < right + 1:
            mid = left + (right - left) // 2
            m_val = nums[mid]
                        
            if (nums[0] > m_val) != (nums[0] > target):
                if nums[0] > target:
                    m_val = -float('inf')
                else:
                    m_val = float('inf')
                                        
            if m_val == target:
                return mid
            elif m_val < target:
                left = mid + 1
            else:
                right = mid - 1
                            
        return -1
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        left, right = 0, len(matrix) - 1
        
        while left < right + 1:
            mid = left + (right - left) // 2
            m_val = matrix[mid][0]
            
            if m_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == 0: 
            return matrix[0][0] == target
        
        if left < len(matrix) and matrix[left][0] == target:
            return True
        else:
            row = left - 1
            left, right = 0, len(matrix[0]) - 1

            while left < right + 1:
                mid = left + (right - left) // 2
                m_val = matrix[row][mid]
                
                if target == m_val:
                    return True
                elif target > m_val:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return False
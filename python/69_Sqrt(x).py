class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid*mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
                
        return ans
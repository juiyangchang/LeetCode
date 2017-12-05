class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        if not triangle or not triangle[0]:
            return 0
        
        ans = [0] * len(triangle[-1])
        ans[0] = triangle[0][0]
        
        for row in triangle[1:]:
            ans[len(row)-1] = ans[len(row)-2] + row[len(row)-1]
            for i in range(len(row)-2, 0, -1):                
                ans[i] = min(ans[i], ans[i-1]) + row[i]
            ans[0] = ans[0] + row[0]
                               
        return min(ans)       
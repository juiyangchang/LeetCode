class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        ans = [1] + [0] * (n-1)
        pt_2 = pt_3 = pt_5 = 0
        
        for i in range(1, n):
            next_2, next_3, next_5 = 2*ans[pt_2], 3*ans[pt_3], 5*ans[pt_5]
            ans[i] = min(next_2, next_3, next_5)
            
            pt_2 += (next_2 == ans[i])
            pt_3 += (next_3 == ans[i])
            pt_5 += (next_5 == ans[i])
        return ans[-1]
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = e0*9 + e1*9 + e2*6
                f1 = e0
                f2 = e0
            else:
                f0 = e0*(c != '0') + e1 + e2*(c < '7')
                f1 = e0*(c == '1')
                f2 = e0*(c == '2')
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0
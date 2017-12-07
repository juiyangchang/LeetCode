class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        # length of seqeucne to guess goes from 1 to n
        for l in range(2, n+1):
            # starting point goes from 1 to n-l+1
            for s in range(1, n-l+2):
                # ending point
                e = s + l - 1
                dp[s][e] = float('inf')
                for k in range(s, e+1):
                    if k == s:
                        penalty = k + dp[k+1][e]
                    elif k == e:
                        penalty = k + dp[s][k-1]
                    else:
                        # there is always a chane that the actual number lies in the range with larger
                        # potential cost
                        penalty = k + max(dp[s][k-1], dp[k+1][e])
                    
                    # make the guess that will minimize the payment
                    if penalty < dp[s][e]:
                        dp[s][e] = penalty
        return dp[1][n]
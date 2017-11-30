from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        lookup = defaultdict(int)
        b_list = []
        for idx, no in enumerate(secret):
            if no == guess[idx]:
                A += 1
            else:
                lookup[no] += 1
                b_list.append(idx)
                
        B = defaultdict(int)
        for idx in b_list:
            g = guess[idx]
            if B[g] < lookup[g]:
                B[g] += 1
                
        return str(A) +'A' + str(sum(B.values())) + 'B'      
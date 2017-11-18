class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        res = 0
        MOD = 10**9 + 7

        mat = [[0]*n for _ in range(m)]
        mat[i][j] = 1

        for _ in range(N):
            new_mat = [[0]*n for _ in range(m)]
            for i, row in enumerate(mat):
                for j, val in enumerate(row):
                    for next_i, next_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 > next_i or m == next_i or 0 > next_j or n == next_j:
                            res = (res + val) % MOD
                        else:
                            new_mat[next_i][next_j] = (new_mat[next_i][next_j] + val) % MOD

            mat = new_mat

        return res

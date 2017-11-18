class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            if cache[i][j] != -1:
                return cache[i][j]

            res = 1
            for next_i, next_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= next_i < m and 0 <= next_j < n and matrix[i][j] < matrix[next_i][next_j]:
                    length = 1 + dfs(next_i, next_j)
                    if length > res:
                        res = length
            cache[i][j] = res
            return res

        if not matrix or not matrix[0]:
            return 0

        cache = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        m, n = len(matrix), len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp = dfs(i, j)
                if tmp > res:
                    res = tmp

        return res

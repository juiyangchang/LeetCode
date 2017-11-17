class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(i, j, visited):
            visited[i][j] = True

            for next_i, next_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0]) \
                    and visited[next_i][next_j] == False and matrix[next_i][next_j] >= matrix[i][j]:
                        dfs(next_i, next_j, visited)


        if not matrix or not matrix[0]:
            return []

        p_visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        a_visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            dfs(i, 0, p_visited)
            dfs(i, len(matrix[0])-1, a_visited)

        for j in range(len(matrix[0])):
            dfs(0, j, p_visited)
            dfs(len(matrix)-1, j, a_visited)

        res = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if p_visited[i][j] and a_visited[i][j]]

        return res

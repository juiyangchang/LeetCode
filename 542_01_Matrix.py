import math

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if not matrix or not matrix[0]:
            return []

        dist = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        queue = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        for x, y in queue:
            for nx, ny in [(x + 1, y), (x-1, y), (x, y+1), (x, y-1)]:

                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and \
                    matrix[nx][ny] == 1 and dist[nx][ny] > dist[x][y] + 1:
                        if math.isinf(dist[nx][ny]):
                            queue.append((nx, ny))

                        dist[nx][ny] = dist[x][y] + 1

        return dist

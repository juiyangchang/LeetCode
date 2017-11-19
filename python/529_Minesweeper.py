class Solution:
    def __init__(self):
        self.moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1),
                     (1, -1), (-1, 1)]

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return [[]]

        i, j = click[0], click[1]
        m, n = len(board), len(board[0])

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        count = 0
        for di, dj in self.moves:
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'M':
                count += 1

        if count != 0:
            board[i][j] = str(count)
        else:
            board[i][j] = 'B'
            for di, dj in self.moves:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'E':
                    self.updateBoard(board, [next_i, next_j])

        return board

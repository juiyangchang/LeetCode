class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def has_duplicate(block):
            block = list(filter(lambda x: x != '.', block))
            return len(block) != len(set(block))

        if not board or not board[0]:
            return False
        
        n = len(board)
        
        if any(has_duplicate(board[i][j] for j in range(n))
            or has_duplicate(board[j][i] for j in range(n))
            for i in range(n)):
            return False
        
        blocks = n // 3
        
        return not any(has_duplicate(board[3*I+i][3*J+j]  for i in range(3) for j in range(3))        
            for I in range(blocks)
            for J in range(blocks)
        )
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # ORIGINAL | NEW | STATE
        #     0       0       0
        #     1       0       1
        #     0       1       2
        #     1       1       3

        # 1 ---- live if 2,3 else die
        # 0 ---- live if 3

        rows = len(board)
        cols = len(board[0])

        def countNeighbors(r, c):
            nei = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for r in range(rows):
            for c in range(cols):
                nei = countNeighbors(r, c)

                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3

                elif nei == 3:
                    board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0

                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        # PHASE 1: Find unsurrounded regions (O > T) and mark as unsurrounded
        # DFS 

        def dfsCapture(r,c):
            # BASE CASE 
            # If out of bounds, or not O
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or board[r][c] != "O"):
                return 
            
            # then it must be O 
            board[r][c] = "T"

            # check surrounding cells
            dfsCapture(r + 1, c)
            dfsCapture(r - 1, c)
            dfsCapture(r, c + 1)
            dfsCapture(r, c - 1)

        # Check border
        for r in range(ROWS):
            if board[r][0] == "O":
                dfsCapture(r,0)
            if board[r][COLS-1] == "O":
                dfsCapture(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfsCapture(0, c)
            if board[ROWS-1][c] == "O":
                dfsCapture(ROWS-1,c) 


        # PHASE 2: Capture the surrounded regions (O > X)
        # PHASE 3: Convert T back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
                if board[r][c] == "T":
                    board[r][c] = "O"


        
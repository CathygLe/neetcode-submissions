class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []  # Stores all valid board configurations
        board = [["."] * n for i in range(n)]  # Initialize n x n board with "."

        # Backtracking helper function to place queens row by row
        def backtrack(r):
            # If all rows are filled, add the board configuration to the result
            if r == n:
                copy = ["".join(row) for row in board]  # Convert each row to a string
                res.append(copy)  # Add this valid configuration to results
                return

            # Try placing a queen in each column of the current row
            for c in range(n):
                if self.isSafe(r, c, board):  # Check if it's safe to place a queen
                    board[r][c] = "Q"  # Place the queen
                    backtrack(r + 1)   # Recurse to the next row
                    board[r][c] = "."  # Backtrack: remove the queen

        backtrack(0)  # Start placing queens from row 0
        return res  # Return all valid configurations

    # Function to check if placing a queen at (r, c) is safe
    def isSafe(self, r: int, c: int, board):
        # Check for another queen in the same column above
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        # Check upper-left diagonal for conflicts
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check upper-right diagonal for conflicts
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True  # No conflicts; it's safe to place a queen
        
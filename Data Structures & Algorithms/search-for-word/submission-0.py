class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        # contains path for word 
        path = set()

        # r, c = coordinates 
        # i = letter in word
        def dfs(r, c, i):

            # base case:
            if i == len(word):
                return True

            if (r < 0 or
                c < 0 or 
                r >= ROWS or 
                c >= COLS or 
                word[i] != board[r][c] or
                (r,c) in path):

                return False
            
            # add the coordinate to the path if the letter is found
            path.add((r,c))
            # search for next letter
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            # must clear path for coordinates aside from r and c +1 surrounding
            path.remove((r,c))

            return res

        # seach each coordinate 
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
            

        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        # DFS function: r, c = current cell coordinates
        # visit = set we're marking (either pac or atl)
        # prevHeight = height of the previous cell (so we know if water can flow to current)
        def dfs(r, c, visit, prevHeight):
            # Base case: 
            # - Out of bounds
            # - Already visited
            # - Current cell is lower than previous 
            if ((r,c) in visit or
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight):
                return 

            # if passes base case, it is reachable
            visit.add((r,c))

            # check surrounding cells
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # check top and bottom border
        for c in range(COLS):
            # first row is pacific ocean touching
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        
        # check left and right border
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        # Final result: cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        
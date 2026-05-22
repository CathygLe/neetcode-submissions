class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        ## up, down, left, right
        directions = [[0,-1],[0,1], [-1,0],[1,0]]

        islands = 0

        def search(x, y):
            if x >= ROWS or y >= COLS or x < 0 or y < 0 or grid[x][y] == "0":
                return 
                
            grid[x][y] = "0"
            for xdirection, ydirection in directions:
                
                search(x + xdirection, y + ydirection)

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == "1":
                    search(r,c)
                    islands += 1

        return islands
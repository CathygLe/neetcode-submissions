class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # down, up, left, right
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        islands = 0 

        ROWS = len(grid)
        COLS = len(grid[0])

        def search(x,y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == "0":
                return 

            grid[x][y] = "0" 

            for xStep, yStep in directions:
                search(x + xStep, y + yStep)
        

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    search(i, j)
        return islands 
            
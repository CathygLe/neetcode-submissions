class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # down, up, left, right
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        maxArea = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def search(x,y,area):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == 0:
                return area

            grid[x][y] = 0 
            area += 1

            for xStep, yStep in directions:
                area = search(x + xStep, y + yStep, area)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, search(i,j, 0))

        return maxArea 
            
                
                    

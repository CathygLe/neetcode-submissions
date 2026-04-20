class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # directions up, down left, right
        directions = [ [0,-1], [0, 1], [1, 0], [-1, 0]]

        rows = len(grid)
        cols = len(grid[0])

        islands = 0


        def dfs(r,c):
            # Base case: not an island or out of bounds.. 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # for each surrounding island, turn it into 0
            for dr, dc in directions:
                grid[r][c] = "0"
                dfs(r + dr, c + dc)
        
        # check each island
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
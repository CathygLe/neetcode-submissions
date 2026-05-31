class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        q = collections.deque()
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if row >= ROWS or col >= COLS or row < 0 or col < 0 or grid[row][col] == 2 or grid[row][col] == 0:
                        continue 
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row,col))
            time += 1

        return time if fresh == 0 else -1
                
            



        
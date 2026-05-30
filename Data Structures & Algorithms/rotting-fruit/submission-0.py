class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        q = collections.deque()
        fresh = 0


        # find rotten and count fresh
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 2:
                    q.append([r,c])
                
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:

                    row = dr + r
                    col = dc  + c

                    #if out of bounds or not fresh fruit
                    if (row < 0 or row >= ROWS
                        or col < 0 or col >= COLS or 
                        grid[row][col] != 1):
                        continue 
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else - 1





        
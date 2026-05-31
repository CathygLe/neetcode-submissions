class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        q = collections.deque()

        def add(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visit or grid[r][c] != 2147483647:
                return 
            
            visit.add((r,c))
            q.append((r,c))
        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visit.add((row,col))

        dist = 0
        # while q is not empty
        while q: 
            #iterate thru q (gates)
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = dist

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1
        
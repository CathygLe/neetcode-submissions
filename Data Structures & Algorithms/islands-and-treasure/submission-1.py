class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        q = collections.deque()

        def addRoom(r,c): 
            # if out of bounds, or visited, or if obstacle
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1):
                #invalid
                return
            #add and append to the q
            visit.add((r, c))
            q.append([r, c])



        # find the treasure chests = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        
        dist = 0
        # while q is not empty
        while q: 
            #iterate thru q (gates)
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            dist +=1


        
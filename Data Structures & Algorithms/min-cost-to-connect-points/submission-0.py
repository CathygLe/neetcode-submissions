class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)

        # map of list where key = i point [cost, node]
        adj = { i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minHeap = [[0,0]] # cost, point

        # Prim's algorthim 
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)

            # skip if already visited
            if i in visit:
                continue 
            
            res += cost
            visit.add(i)
            
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res
            
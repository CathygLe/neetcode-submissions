class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # nodes are labelled 1 to n, therefore n + 1
        N = len(edges)

        # Root node for each node
        par = [i for i in range(N+1)]
        # height of each node
        rank = [1]*(N+1)


        # find the root node 
        def find(n):
            if n == par[n]:
                return par[n]

            par[n] = find(par[n])

            return par[n]

        # return True if not connected

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
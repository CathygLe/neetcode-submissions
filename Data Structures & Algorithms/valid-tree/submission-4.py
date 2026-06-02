class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 
        
        adj = { i:[] for i in range(n)}
        # made children nodes to parent
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node,prev):
            if node in visit:
                return False 
            
            visit.add(node)

            for n in adj[node]:
                if n == prev:
                    continue
                
                if dfs(n, node) == False:
                    return False 
            return True 
        return dfs(0, -1) and len(visit) == n

        
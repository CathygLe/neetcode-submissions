class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # find the root parent of node n1
        def find(n1):
            # result = n1
            res = n1

            # while the node is not it's self 
            # traversing the tree until we find root parent
            while res != par[res]:
                # set the current node to it's parent's parent
                par[res] = par[par[res]]
                res = par[res]
            return res

        # combine trees
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            # same parent
            if p2 == p1:
                return 0
            
            if rank[p2] > rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else: 
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n
        for n1,n2 in edges:
            res -=union(n1,n2)
        return res
            
        
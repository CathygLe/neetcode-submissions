class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        # to make it in alpha order
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            # Base case: no more tickets
            if len(res) == len(tickets) + 1:
                return True
            # # edge case: dead end
            # if src not in adj:
            #     return False
            
            temp = list(adj[src])
            for index, neighbour in enumerate(temp):
                adj[src].pop(index)
                res.append(neighbour)

                if dfs(neighbour): return True

                # backtrack if deadend
                adj[src].insert(index,neighbour)
                res.pop()
            return False
        
        dfs("JFK")

        return res


        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top floor is after n + 1

        # we will dirrectly modify the input array
        n = len(cost)
        # 0 indicates the last floor
        cost.append(0)

        # [0, 1, 2, 3, 4, 0]
        # starting with last 2 floors (position 3) (not destination floor)
        for i in range(n-3,-1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        
        return min(cost[0], cost[1])




        
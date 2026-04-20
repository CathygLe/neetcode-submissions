class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create array tracking what's reachable 
        # inf means not reachable
        prices = [float("inf")] * n
        # source node cost = 0 
        prices[src] = 0

        # search flights that will reach dest within k + 1 (+1 is the dest)
        # i = layer 
        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                # we compare prices since it's the "confirmed reachable nodes"
                # if we do tmp, we're accidentally going another level 
                # Check if reachable from node s
                if prices[s] == float("inf"):
                    continue

                # update price if its lower or reachable
                # remember to take the confirmed prices!!! since checkprices is not confirmed and still changing
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]


# tmpPrices is used so we don't alter prices, in case a path is a deadend 
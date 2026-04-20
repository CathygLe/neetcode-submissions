class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # max heap doesnt exist in python.. so we simulate it by turning it negative

        stones = [ -s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            # get the first and second largerst
            # since its a min heap, we need to take abs (since we turned it neg)
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            # if =.. do nothing
            # else.. append difference

            if first > second:
                neg = second - first
                heapq.heappush(stones, neg)

        # edge case: stones is empty
        stones.append(0)
        return abs(stones[0])        
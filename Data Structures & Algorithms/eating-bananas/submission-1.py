class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        result = r 

        while l <= r:
            hours = 0

            midRate = l + (r-l)//2

            for p in piles:
                hours += math.ceil(p/midRate)
            
            if hours <= h:
                result = midRate
                r = midRate - 1 
            else:
                l = midRate + 1

        return result 
        
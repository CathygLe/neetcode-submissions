class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]

        best = 0

        for num in prices:
            minP = min(num, minP)

            dayP = num - minP

            best = max(best, dayP)
        
        return best



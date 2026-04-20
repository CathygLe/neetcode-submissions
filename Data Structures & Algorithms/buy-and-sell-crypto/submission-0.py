class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        lowestPrice = prices[0]
        for num in prices: 
            lowestPrice = min(lowestPrice, num)

            best = max((num-lowestPrice), best)

        return best



        
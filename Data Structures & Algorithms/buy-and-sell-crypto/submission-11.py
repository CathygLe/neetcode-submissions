class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsf = prices[0]
        profit = 0 

        for price in prices:
            minsf = min(price, minsf)

            profit = max(price - minsf, profit)
        
        return profit 

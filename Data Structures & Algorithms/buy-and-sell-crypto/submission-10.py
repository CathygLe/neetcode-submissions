class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsf = prices[0]
        profit = 0 

        for price in prices:
            if price < minsf:
                minsf = price 

            profit = max(profit, price - minsf)
        return profit 
            

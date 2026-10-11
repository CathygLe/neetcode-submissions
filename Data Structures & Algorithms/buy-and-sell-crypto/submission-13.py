class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsf = prices[0]

        result = 0 

        for price in prices:
            if price < minsf:
                minsf  = price 
            
            result = max(result, price - minsf)
        return result 

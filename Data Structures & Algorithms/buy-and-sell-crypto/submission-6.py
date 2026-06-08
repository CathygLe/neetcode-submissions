class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]

        result = 0 

        for price in prices:
            if price < minprice:
                minprice = price 
            
            profit = price - minprice

            result = max(profit, result)
        
        return result
         

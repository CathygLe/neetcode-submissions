class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumPrice = prices[0]
        maxProfit = 0 

        for price in prices:
            profit = price - minimumPrice

            if profit > maxProfit:
                maxProfit = profit 
            
            if minimumPrice > price:
                minimumPrice = price
        return maxProfit 

         

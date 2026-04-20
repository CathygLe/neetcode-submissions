class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            profit = price - minimum 

            if profit > maximum:
                maximum = profit
            
            if price < minimum:
                minimum = price

        
        return maximum

        
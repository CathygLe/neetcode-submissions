class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            diff = price - minimum

            if price < minimum:
                minimum = price

            if diff > maximum:
                maximum = diff
                
        return maximum

         

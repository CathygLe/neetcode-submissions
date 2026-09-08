class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsf = prices[0]
        result = 0

        for price in prices:
            difference = price - minsf 

            result = max(difference, result)

            if price < minsf:
                minsf = price
        return result

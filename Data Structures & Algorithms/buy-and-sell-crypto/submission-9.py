class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        minsf = prices[0]

        for num in prices:
            profit = num - minsf

            if profit > result: 
                result = profit 
            minsf = min(minsf, num)

        return result 
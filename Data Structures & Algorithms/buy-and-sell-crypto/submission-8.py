class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsf = prices[0]

        maxsf = 0 


        for num in prices:
            if num - minsf > maxsf:
                maxsf = num - minsf 
            
            if num < minsf:
                minsf = num
        return maxsf
         

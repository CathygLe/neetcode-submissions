class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = float("-inf")

        sumsf = 0
        for num in nums:
            sumsf += num 

            maxsf = max(maxsf, sumsf)

            if sumsf < 0:
                sumsf = 0 
                continue 

        return maxsf 
            
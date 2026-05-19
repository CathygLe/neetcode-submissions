class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]
        sumsf = nums[0]
        
        i = 1
        while i < len(nums):
            if sumsf < 0:
                sumsf = 0

            sumsf += nums[i]
            maxsf = max(maxsf, sumsf)
            i += 1
        
        return maxsf

        
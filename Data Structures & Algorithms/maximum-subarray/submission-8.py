class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]

        for i in range(len(nums)):
            sumsf = 0
            for j in range(i, len(nums)):
                sumsf += nums[j]
            
                maxsf = max(sumsf, maxsf)
        

        return maxsf
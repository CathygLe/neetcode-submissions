class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]

        sumsf = 0 

        for num in nums:
            if sumsf < 0:
                sumsf = num
            else: 
                sumsf += num
            
            maxsf = max(maxsf, sumsf)
        
        return maxsf
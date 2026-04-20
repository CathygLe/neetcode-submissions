class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            # sum(n to 0) - sum(nums) = result.. so we do it one at a time
            res += (i - nums[i])
        
        return res
        
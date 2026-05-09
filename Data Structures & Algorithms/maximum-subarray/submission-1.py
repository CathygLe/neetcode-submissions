class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]

        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num

            maxsf = max(curSum, maxsf)
        return maxsf
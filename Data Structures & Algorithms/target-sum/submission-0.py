class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, curSum) -> number of ways

        def backtrack(i, curSum):
            # already visited 
            if (i, curSum) in dp:
                return dp[(i, curSum)]

            # base case: reached the end
            if i >= len(nums):
                return 1 if curSum == target else 0

            # Save before returning
            dp[(i, curSum)] = (backtrack(i + 1, curSum + nums[i]) +
                backtrack(i + 1, curSum - nums[i]))  
            return dp[(i, curSum)]

        return backtrack(0,0)      



        # brute force
        # def backtrack(i, curSum):
        #     # base case: reached the end
        #     if i >= len(nums):
        #         return 1 if curSum == target else 0

        #     return (
        #         backtrack(i + 1, curSum + nums[i]) +
        #         backtrack(i + 1, curSum - nums[i]))  

        # return backtrack(0,0) 
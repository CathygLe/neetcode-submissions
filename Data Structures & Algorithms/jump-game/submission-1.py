class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal is initially to reach the end
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1): 
            # if we can jump to the goal
            if i + nums[i] >= goal:
                goal = i


        return True if goal == 0 else False
        
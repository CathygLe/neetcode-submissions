class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l = i + 1
            r = len(nums) - 1

            while l < r:

                while l < r and l != i+1 and nums[l] == nums[l-1]:
                    l += 1
                
                while l < r and r != len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1

                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                r -= 1
                l += 1

        return res 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        result = []



        for i in range(len(nums)):
            val = nums[i]

            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                summed = val + nums[l] + nums[r]

                if summed == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif summed > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result 


                    
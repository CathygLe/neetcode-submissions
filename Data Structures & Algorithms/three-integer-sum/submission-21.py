class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        result = []


        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                summed = nums[i] + nums[l] + nums[r]

                if summed == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif summed > 0:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                else:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        return result 


            
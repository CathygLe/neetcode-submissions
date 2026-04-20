class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i !=0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while (l<r):
                total = nums[i] + nums[r] + nums[l]

                if total == 0:
                    output.append([nums[i],nums[r], nums[l]])
                    r -=1
                    l += 1
                elif total > 0:
                    r -=1
                else:
                    l +=1
                
        return output

            
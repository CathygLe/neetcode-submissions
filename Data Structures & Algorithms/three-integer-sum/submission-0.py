class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer =[]
        nums.sort()


        for i in range(len(nums)):

            l = i + 1
            r = len(nums) - 1

            if i !=0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if (total == 0):
                    answer.append([nums[i], nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while( nums[l] == nums[l+1]):
                        l += 1
                if (total > 0):
                    r -= 1
                if (total < 0):
                    l += 1
        return answer

                


        
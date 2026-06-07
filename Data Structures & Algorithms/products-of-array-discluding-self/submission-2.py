class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        start = 1
        for i in range(len(nums)): 
            result[i] = start 
            start *= nums[i]

        end = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= end
            end *= nums[j]

        return result


        
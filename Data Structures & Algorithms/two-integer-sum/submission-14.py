class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(nums)):
            value =  target - nums[i]

            if value in compliments:
                return [compliments[value],i]
            else:
                compliments[nums[i]] = i 
        



            
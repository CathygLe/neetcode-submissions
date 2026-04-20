class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            result = target - num 
            if result in hashMap:
                return [hashMap[result], i]

            hashMap[num] = i 





 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 

        while l < r:
            val = numbers[l] + numbers[r]

            if val == target:
                return [numbers[l], numbers[r]]
            elif val > target:
                r -=1
            else:
                l +=1
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            com = target - num

            if com in visited:
                return [visited[com], i]
            else:
                visited[num] = i 
        

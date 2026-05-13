class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        def back(index, curr, total):
            if total == target:
                result.append(curr.copy())
                return 
            
            if index >= len(nums) or total > target:
                return

            
            curr.append(nums[index])
            back(index, curr, total + nums[index])

            curr.pop()
            back(index+1, curr, total)


        back(0, [], 0)

        return result

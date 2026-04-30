class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, arr):
            total = sum(arr)

            if total == target:
                result.append(arr)
                return
            
            if i >= len(nums) or total > target:
                return

            # include (stay at i)
            dfs(i, arr + [nums[i]])

            # exclude (move forward)
            dfs(i + 1, arr)

        dfs(0, [])
        return result

        
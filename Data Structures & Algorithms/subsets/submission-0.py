class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        # i = index of value
        def dfs(i):
            # if out of bounds, subset completed
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # append the first value
            subset.append(nums[i])
            dfs(i + 1)

            # backtrack and remove
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res



            
        
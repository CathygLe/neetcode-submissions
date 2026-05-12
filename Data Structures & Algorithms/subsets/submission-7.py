class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def back(index, curr):
            if index >= len(nums):
                result.append(curr.copy())
                return

            
            curr.append(nums[index])

            back(index + 1, curr)

            curr.pop()
            back(index + 1, curr)

        back(0, [])

        return result

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setted = set(nums)

        if len(setted) < len(nums):
            return True
        else:
            return False
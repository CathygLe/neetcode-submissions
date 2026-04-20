class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # uses XOR
        res = 0
        for num in nums:
            res = num ^ res
        return res
        
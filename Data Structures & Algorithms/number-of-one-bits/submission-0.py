class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2

            # shift number to right 
            n = n >> 1
        return res 

        
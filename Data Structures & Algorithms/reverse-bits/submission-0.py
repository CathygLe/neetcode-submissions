class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(32):
            # get the ith bit
            bit = ( n >> i) & 1

            # place bit at the end of res
            res = res | (bit << (31 - i))
        
        return res 
        
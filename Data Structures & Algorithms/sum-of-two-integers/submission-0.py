class Solution:
    def getSum(self, a: int, b: int) -> int:

        # b will track carry
        while (b != 0):
            temp = (a & b) << 1
            a = a ^ b; 
            
            b = temp

        return a

        
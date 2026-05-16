class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 = 1                                            1
        # 2 = 11, 2                                        2 
        # 3 = 12, 21, 111                                  3 
        # 4 = 1111, 22, 112, 211, 121,                     5 
        # 5 = 1111, 221, 122, 212, 1112, 1121, 1211, 2111, 8

        first = 1
        second = 1 

        for i in range(n-1):
            temp = first 

            first = second
            second = temp + second 
        
        return second
class Solution:
    def climbStairs(self, n: int) -> int:
        # step n = 1 since only 1 path exists
        # step n - 1 = 1 since only 1 path to n exists
        #     one, two = 1, 1

        #     for i in range(n-1):
        #         temp = one
                
        #         one = one + two
        #         two = temp

        #     return one  
            

        # 1 1                 1
        # 2 1 1, 2            2 
        # 3 1 2, 2 1, 1 1 1   3 
        # 4 1 1 1 1, 2 2, 112, 211, 121, 5 
        # 5 1111, 221, 122, 212, 1112, 1121, 1211, 2111, 8

        first = 1
        second = 1 

        for i in range(n-1):
            temp = first 

            first = second
            second = temp + second 
        
        return second
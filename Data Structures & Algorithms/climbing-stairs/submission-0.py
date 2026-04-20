class Solution:
    def climbStairs(self, n: int) -> int:
        # step n = 1 since only 1 path exists
        # step n - 1 = 1 since only 1 path to n exists
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            
            one = one + two
            two = temp

        return one  
        
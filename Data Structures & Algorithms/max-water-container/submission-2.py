class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 

        l = 0
        r = len(heights) -1
        output = 0


        while l < r:
            output = max( output, min(heights[l], heights[r]) * (r-l))

            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return output 


        
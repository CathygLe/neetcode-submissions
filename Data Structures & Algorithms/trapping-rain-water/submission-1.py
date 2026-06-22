class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        maxLeft = [0]*n
        maxRight = [0]*n


        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        maxRight[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            maxRight[j] = max(maxRight[j+1],height[j])

        result = 0 

        for i in range(len(height)):
            result += min(maxLeft[i],maxRight[i]) - height[i]

        return result
        

        
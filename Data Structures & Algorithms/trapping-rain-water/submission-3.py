class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        maxLeft = n * [0]
        maxRight = n * [0]

        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        maxRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        result = 0 
        for i in range(n):
            result += min(maxRight[i], maxLeft[i]) - height[i]

        return result 
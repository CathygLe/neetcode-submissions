class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0 
        r = rows*cols - 1

        while l <= r:
            mid = l + (r-l)// 2

            xCord = mid // cols 
            yCord = mid % cols 
            val = matrix[xCord][yCord]

            if val == target:
                return True 
            elif val > target: 
                r = mid - 1 
            else:
                l = mid + 1
        return False


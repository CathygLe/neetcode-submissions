class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2

            midCol = mid % COLS
            midRow = mid // COLS

            if target == matrix[midRow][midCol]:
                return True
            elif target > matrix[midRow][midCol]:
                l = mid + 1
            else: 
                r = mid - 1
        
        return False

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])


        l = 0 
        r = rows * cols -1 

        while l <= r:
            mid = l + (r-l)//2 

            midCol = mid%cols
            midRow = mid//cols 

            if matrix[midRow][midCol] == target: 
                return True 
            elif target > matrix[midRow][midCol]:
                l = mid + 1 
            else: 
                r = mid - 1
        
        return False 

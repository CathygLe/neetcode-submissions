class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])

        l = 0 
        r = row*cols - 1

        while l <= r:
            mid = l + (r-l)//2 

            xcord = mid//cols
            ycord = mid%cols 

            if matrix[xcord][ycord] == target:
                return True 
            elif matrix[xcord][ycord] > target:
                r = mid - 1 
            else:
                l = mid + 1
        return False 
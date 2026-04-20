class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # left and right boundary
        l = 0 
        r = len(matrix) - 1

        while l < r:
            for i in range(r-l):
                top = l
                bottom = r

                #save the topleft value 
                topLeft = matrix[top][l+i]

                #move bottom left into top left
                matrix[top][l +i] = matrix[bottom - i][l]

                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r -i]

                #move top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                # move top left into top right
                matrix[top+i][r] = topLeft
            l += 1
            r -=1
        
        
        
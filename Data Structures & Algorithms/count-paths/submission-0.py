class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom row will only have 1 option (since they can only go right)
        row = [1] * n

        # for every row (last row excluded since ^^^)
        for i in range(m-1):
            newRow = [1] * n

            # last column is 2, since u can only go down, therefore -2 (also, -2 because in range(start, increment, end)
            # start is inclusive, end is not inclusive 
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            
            row = newRow
        return row[0]

        
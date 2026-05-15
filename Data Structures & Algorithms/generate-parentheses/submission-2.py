class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def back(openB, closed, curr):
            if openB == n and closed == n:
                res.append(curr)
                return
            
            if openB < n: 
                back(openB + 1, closed, curr + "(")

            if openB > closed:
                back(openB, closed + 1, curr + ")")
        back(0,0, "")

        return res
            

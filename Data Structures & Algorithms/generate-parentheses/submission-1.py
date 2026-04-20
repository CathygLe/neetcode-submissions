class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def backtrack(openN, closedN, rsf):
            if openN == n and closedN == n:
                res.append(rsf)
                return

            if openN < n:
                backtrack(openN+1, closedN, rsf + "(")

            if closedN < openN:
                backtrack(openN, closedN+1, rsf + ")")
            
            return res
        backtrack(0,0,"")
        return res



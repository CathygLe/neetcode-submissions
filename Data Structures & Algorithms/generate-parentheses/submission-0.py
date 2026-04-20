class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtrack(openN, closedN, current):
            if openN == closedN == n:
                result.append(current)
                return 
            
            if openN < n:
                backtrack(openN + 1, closedN, current + "(")

            if closedN < openN:
                backtrack(openN, closedN + 1, current + ")")

        backtrack(0,0,"")
        return result 


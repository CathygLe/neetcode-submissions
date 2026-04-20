class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"}

        
        def backtrack(i, acc):
            # base case
            if len(acc) == 2:
                res.append(acc)
                return 
            
            # iterate thru each letter corresponding to digit[i]
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, acc + c)

        
        if digits:
            backtrack(0, "")
        
        return res

        
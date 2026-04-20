class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sArray = list(s)   
        temp = set()
        if len(sArray) == 0:
            res = 0
        else:
            res = 1
            
        for letter in sArray: 
            if letter in temp:
                res = max(res, len(temp))
                temp = set()

            temp.add(letter)

        
        return res

        
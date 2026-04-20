class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sArray = list(s)   
        temp = set()
        res = 0

        for letter in sArray: 
            if letter in temp:
                temp = set()
            
            temp.add(letter)
            res = max(res, len(temp))
        
        return res

        
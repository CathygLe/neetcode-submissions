class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sArray = list(s)   
        temp = set()
        res = 0
        start = 0

        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[start])
                start +=1

            temp.add(s[i])
            res = max(res, len(temp))
            
        return res

        
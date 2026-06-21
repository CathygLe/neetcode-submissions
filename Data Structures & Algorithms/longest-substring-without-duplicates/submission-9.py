class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        temp = []

        start = 0 
        maxsf  = 0 

        for letter in s:
            while letter in temp:
                temp.remove(s[start])
                start += 1 

            temp.append(letter)
            maxsf = max(maxsf, len(temp))
        return maxsf


            
            
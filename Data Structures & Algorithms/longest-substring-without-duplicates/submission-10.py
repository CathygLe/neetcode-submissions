class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        temp = []

        maxsf = 0 
        front = 0 
        for i in range(len(s)):
            letter = s[i]

            while letter in temp and front < i: 
                temp.remove(s[front])
                front +=1 
            
            temp.append(letter)
            maxsf = max(maxsf, len(temp))

        return maxsf

            
            
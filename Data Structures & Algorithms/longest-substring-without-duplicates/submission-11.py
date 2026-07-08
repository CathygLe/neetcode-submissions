class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        front = 0
        substring = set() 
        result = 0

        for letter in s:
            if letter in substring:
                while letter in substring: 
                    substring.remove(s[front])
                    front +=1

            substring.add(letter)
            result = max(len(substring), result)
        return result 


## mistake earlier... not adding the current letter, even tho it exists earlier in the string 
## !!! the curr letter should always be appended




            
            
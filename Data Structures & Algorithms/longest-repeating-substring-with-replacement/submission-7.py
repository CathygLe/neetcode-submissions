class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        longest = 0

        for letter in letters:
            replacements = 0 
            start = 0 

            for end in range(len(s)):
                let = s[end]
                if let != letter:
                    replacements += 1
                
                while replacements > k: 
                    if s[start] != letter:
                        replacements -= 1 
                        start +=1
                    else:
                        start +=1
                
                longest = max(longest, end - start + 1)
        return longest
                


        
                    

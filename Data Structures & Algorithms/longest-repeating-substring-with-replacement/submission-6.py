class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)

        maxsf = 0
        for letter in letters:
            l = r = replacements = 0 
            
            while r < len(s):

                if s[r] != letter: 
                    replacements += 1
                while replacements > k and r < len(s) and l < r:
                    if s[l] != letter:
                        replacements -= 1 
                        l += 1 
                    else:
                        l += 1
                maxsf = max(maxsf, r-l+1)
                r +=1 
                
        return maxsf

                


        
                    

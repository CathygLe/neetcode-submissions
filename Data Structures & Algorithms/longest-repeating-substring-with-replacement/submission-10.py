class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sets = set(s)
        output = 0

        for letter in sets:

            substring = []
            replacements = 0 
            front = 0 
            for i in range(len(s)):
                let = s[i]

                if let != letter:
                    replacements += 1

                substring.append(let)
                
                while replacements > k:
                    if s[front] != letter:
                        replacements -= 1
                        substring.remove(s[front])

                    front += 1
                output = max(output, i - front + 1)

        return output                 




        
                    

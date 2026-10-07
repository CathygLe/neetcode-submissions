class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mappedT = {}
        mappedS  = {}

        for letter in s:
            mappedS[letter] = mappedS.get(letter, 0) +  1
        
        for letter in  t:
            mappedT[letter] = mappedT.get(letter, 0) +  1


        if mappedT == mappedS:
            return True
        else:
            return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        if len(s) != len(t):
            return False

        for letter in s:
            mapS[letter] = mapS.get(letter, 0) + 1
        for letter in t:
            mapT[letter] = mapT.get(letter, 0) + 1
        
        return True if mapT == mapS else False
        

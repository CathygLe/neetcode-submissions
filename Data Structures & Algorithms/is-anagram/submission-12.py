class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}


        for letter in s:
            sMap[letter] = 1 + sMap.get(letter, 0)

        for letter in t:
            tMap[letter] = 1 + tMap.get(letter, 0)

        if sMap == tMap:
            return True 
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for letter in s:
            if letter not in sMap:
                sMap[letter] = 1
            else:
                sMap[letter] +=1 
        
        for letter in t:
            if letter not in tMap:
                tMap[letter] = 1
            else:
                tMap[letter] +=1 
        
        return tMap == sMap 
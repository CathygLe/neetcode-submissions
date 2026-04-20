class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        map1 = {}
        for letter in s1:
            map1[letter] = map1.get(letter, 0) + 1
        
        size = len(s1)

        for i in range(len(s2)):
            map2 = {}
            count = 0
            
            j = i

            for j in range(i, len(s2)):
                map2[s2[j]] = map2.get(s2[j], 0) + 1

                if map2.get(s2[j], 0) > map1.get(s2[j], 0):
                    break
                
                if map2.get(s2[j], 0) == map1.get(s2[j], 0):
                    count += map2.get(s2[j], 0)

                if count == size:
                    return True

        return False  







        
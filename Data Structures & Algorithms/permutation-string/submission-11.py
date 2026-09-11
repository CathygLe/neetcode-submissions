class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word1 = {}

        for letter in s1:
            word1[letter] = word1.get(letter, 0 ) + 1
        

        for i in range(len(s2) - len(s1) + 1):

            track = {}

            for check in range(i, i + len(s1)):
                letter = s2[check]

                track[letter] = track.get(letter, 0) + 1

                if track[letter] > word1.get(letter,0):
                    break 
                elif word1 == track:
                    return True 
        
        return False 



        
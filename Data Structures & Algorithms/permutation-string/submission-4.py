class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for letter in s1:
            count1[letter] = count1.get(letter, 0) + 1


        for windowStart in range(len(s2)- len(s1)+1):
            windowCount = {}

            for window in range(windowStart, windowStart+len(s1)):
                char = s2[window] 
                windowCount[char] = windowCount.get(char, 0) + 1

                if windowCount[char] > count1.get(char, 0):
                    break
                else:
                    if windowCount == count1:
                        return True
        return False 







        
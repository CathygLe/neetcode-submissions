class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        for i in range(len(s2) - len(s1) + 1):
            count2 = {}
            for j in range(i, i + len(s1)):
                c = s2[j]
                count2[c] = 1 + count2.get(c, 0)
                if count2[c] > count1.get(c, 0):
                    break
            else:  # only executes if inner loop did NOT break
                if count2 == count1:
                    return True
        return False
        





        
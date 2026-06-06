class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}


        for word in strs:
            sortedW = "".join(sorted(word))

            if sortedW not in mapped:
                mapped[sortedW] = [word]
            else:
                mapped[sortedW].append(word)
        
        return list(mapped.values())


        



     
        
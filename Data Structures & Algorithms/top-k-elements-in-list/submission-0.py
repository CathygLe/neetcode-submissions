class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        array = []

        for key, value in count.items():
            array.append([value, key])

        array.sort()

        res = []
        while len(res) < k:
            res.append(array.pop()[1])
        return res
        




        
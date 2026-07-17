class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        total = m + n
        middle = total // 2

        i = j = 0
        prev = curr = 0

        for _ in range(middle + 1):
            prev = curr

            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 1:
            return curr

        return (prev + curr) / 2
            

                
        
        
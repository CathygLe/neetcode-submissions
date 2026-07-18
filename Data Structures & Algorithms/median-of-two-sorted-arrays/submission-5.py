class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        middle = (len1 + len2)// 2

        i = 0 
        j = 0 

        curr = 0
        for count in range(middle + 1):
            prev = curr 

            if i < len1 and (j >= len2 or nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        
        if (len1 + len2) % 2 == 1:
            return curr
        else:
            return (prev+curr)/2
            

                
        
        
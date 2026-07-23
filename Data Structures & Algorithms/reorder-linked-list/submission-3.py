# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arrayed = []

        curr = head

        while curr: 
            arrayed.append(curr)
            curr = curr.next

        l = 0 
        r = len(arrayed) - 1

        
        while l < r:
            arrayed[l].next = arrayed[r]
            l += 1

            if l < r:
                arrayed[r].next = arrayed[l]
                r -= 1
        arrayed[l].next = None
        




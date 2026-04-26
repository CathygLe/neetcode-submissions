# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listed = []
        curr = head

        while curr:
            listed.append(curr)
            curr = curr.next 

        curr = head 

        l = 0
        r = len(listed) - 1

        while l < r:
            listed[l].next = listed[r]
            l +=1 

            if l > r:
                break
            listed[r].next = listed[l]

            r -=1 
        listed[l].next = None 
        


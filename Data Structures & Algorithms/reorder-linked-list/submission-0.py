# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # find the middle of the list
        # must check "fast" cuz what if is it list size 1 or empty?
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # initalize second list 
        second = slow.next

        # End the first list
        prev = slow.next = None

        # Reverse the second list
        while second:
            tmp = second.next 

            second.next = prev 
            prev = second
            second = tmp 

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        
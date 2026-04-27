"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapped = {}
        curr = head 

        while curr:
            if curr not in mapped:
                mapped[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head 

        while curr: 
            if mapped[curr]:
                mapped[curr].next = mapped.get(curr.next)

            if mapped[curr]:
                mapped[curr].random = mapped.get(curr.random)

            curr = curr.next
        return mapped.get(head)
        



        




        
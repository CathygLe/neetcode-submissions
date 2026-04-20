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
        oldToCopy = {None: None}# map original nodes to copied versions
        # need to create copies so we can modify it

        cur = head
        while cur:
            copy = Node(cur.val)       # Create a copy of the current node with the same value
            oldToCopy[cur] = copy      # Store it in the map
            cur = cur.next             # Move to the next node in the original list

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]



        
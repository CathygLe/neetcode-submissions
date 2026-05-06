# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = [] 

        q.append(root)

        while q:
            count = len(q)

            level = []
            for i in range(count):
                node = q.popleft() 
                
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

                if node and i == count - 1:
                    res.append(node.val)
                

        return res

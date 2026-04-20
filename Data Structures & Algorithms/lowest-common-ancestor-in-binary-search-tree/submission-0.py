# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root 

        # BST means left node = smaller than root
        #          right node = larger than root
        while cur:
            # check if value is larger than node > if so search right
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # check if value is smaller than node > if so search left
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            else:
                return cur
        
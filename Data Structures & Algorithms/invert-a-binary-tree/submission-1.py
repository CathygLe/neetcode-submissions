# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # criteria for recursion 
        # 1. Base Case 
        # 2. Recursive call

        # Base case: if root = none, return none
        if not root:
            return None

        tmp = root.right
        root.right = root.left
        root.left = tmp

        # recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        


        
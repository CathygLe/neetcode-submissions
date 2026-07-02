# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0 

        if not root:
            return 0 

        def dfs(curr):
            nonlocal maxD
            if not curr:
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)

            diameter = left + right 

            maxD = max(maxD, diameter)

            return max(left,right) + 1
        dfs(root)

        return maxD
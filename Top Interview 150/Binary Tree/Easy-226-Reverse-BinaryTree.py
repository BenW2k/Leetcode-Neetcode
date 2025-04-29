# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: # terminate the current recursive loop if the root doesn't exist
            return root
        self.invertTree(root.left) # recursion on left branch, if its None then it ends anyway
        self.invertTree(root.right) # ditto
        root.left, root.right = root.right, root.left # Set the left root node to right root node and vice versa

        return root
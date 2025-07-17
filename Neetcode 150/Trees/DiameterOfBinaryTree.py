# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the reason its O(h) and not O(N), like recursion usually can be, is because the the entire tree is not on the stack at the same time
        # The max amount of calls on the stack equates to the height of the tree which is h hence O(h)
        self.res = 0 # we keep this global variable to return
        
        def dfs(curr):
            if not curr: #base case
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right) # We replace self.res if the diameter of the current tree is larger
            return 1 + max(left, right) # this is the height of the tree that we're returning, its the height of the child trees + 1
        dfs(root)
        return self.res
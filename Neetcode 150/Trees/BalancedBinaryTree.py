# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # So we use recursive DFS to find height of the sub trees, then we compare absolute values to find the difference between
        # the subtree heights, if the diff is greater than 1 then we know the tree isn't balanced.
        # We use -1 to 'bubble out' of the recursive loop because we've already met our condition

        def dfs(curr):
            if not curr: #base case
                return 0
            right = dfs(curr.right)
            if (right == -1): #checking if already bubbling up
                return -1
            left = dfs(curr.left)
            if (left == -1):
                return -1
            if abs(left-right) > 1: # computes the difference
                return -1 
            return 1 + max(left, right) # returns height of the tree
        if dfs(root) == -1:
            return False
        else:
            return True
        
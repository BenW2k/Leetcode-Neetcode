# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases
        if not subRoot: # If the subtree is empty it will always be in the tree because its null and so are the left and right of child nodes
            return True
        if not root:
            return False # we can say this is false because if we reach this conditional, we know subtree isn't empty
        if self.sameTree(root, subRoot):
            return True # this is if they're identical, starting from both parent nodes
        # Finally, if we want to check subtrees, we know that isSubtree is recursive so it will check each node down the main tree against the subtree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



        
    def sameTree(self, root, subRoot):
        if not root and not subRoot: # if both are null nodes return true
            return True
        if root and subRoot and root.val == subRoot.val: # if they have the same value, go deeper into the tree
            return (self.sameTree(root.left, subRoot.left)) and self.sameTree(root.right, subRoot.right)
        return False # else return false
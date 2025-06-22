# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        # We use a helper function to assist with recursion

        def helper(l, r):
            if l > r: # Base case, if r ever goes past l we return None to end the recursive sequence
                return None
            m = (l + r) // 2 # Get the mid point
            root = TreeNode(nums[m]) # Set the root node to be the mid point (for balancing)
            root.left = helper(l, m - 1) # recursion down the left side
            root.right = helper(m + 1, r) # recursion down the right side
            return root # returning the BST
        return helper(0, len(nums) - 1) # Returning BST from helper function
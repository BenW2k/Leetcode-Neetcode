# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = collections.deque()
        queue.append(root)
        smallest = min(q.val,p.val)
        largest = max(q.val,p.val)

        while queue:
            node = queue.popleft()
            if node:
                if node.val == smallest or node.val == largest:
                    return node
                elif (node.val > smallest) and (node.val < largest):
                    return node
                elif (smallest < node.val) and (largest < node.val):
                    queue.append(node.left)
                else:
                    queue.append(node.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Basically we're thinking about a BFS but excluding half of the remaining tree every time
        # Logic dictates that if one of the target nodes is larger than curr node and one is smaller then curr node has to be their LCA
        # Logic also dictates that if the current node IS one of the target nodes then it will be the LCA.
        # We need to determine which is the smallest and which is the largest val target node for easier comparisons so we use the min and max funcs
        # We then return the node if it we have found the LCA and if not that means that both of the target nodes are either larger
        # or smaller than the curr node, so we can disregard 1 child and add the other one to the queue to continue our search
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
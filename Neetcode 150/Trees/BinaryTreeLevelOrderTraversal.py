# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #Level order traversal so BFS.
        #Print the levels out separately so we need some way to identify what level we're on
        # the queue should only have a single layer in it at a time at the start of each iteration of the while loop (initially with adding parent node)
        # we can then find the length of queue to ensure that it only loops through the current level
        # we then add a temp level list and loop through, popping each node, adding its val to the level list and adding any of its non-null child
        # nodes to the queue
        # We then do a quick check to see if the level array is empty, if it isn't we can append the level array to the res array and repeat for all levels
        # we then return the res array
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            q_length = len(q)
            level = []
            for i in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
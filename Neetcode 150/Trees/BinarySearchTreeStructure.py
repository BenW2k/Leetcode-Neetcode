# Binary Tree
class TreeNode: # Class for a tree node with basic values for initialisation
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self): # Method for printing the node, so print(TreeNode) will just print the val of the specified node
        return str(self.val)
    

# Recursive DFS Pre Order Traversal Time: O(n), Space: O(n)
def pre_order(node):
    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursive DFS In Order Traversal Time: O(n), Space: O(n)

def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)

# Recursive DFS Post Order Traversal Time: O(n), Space: O(n)

def post_order(node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)

# Test Case
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# pre_order(A)
# in_order(A)
# post_order(A)

# Iterative DFS Pre order traversal Time: O(n), Space: O(n)
# Tip: This may look counter-intuitive but you are appending the right node to the stack before the left node to keep the left-most nodes always at the top of the stack
# while there are still left nodes to iterate through, once the left nodes are exhausted, the right nodes and their children will be traversed.

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
# pre_order_iterative(A)


# BFS Level Order Traversal Time: O(n), Space: O(n)

from collections import deque # import the double ended queue data structure for as queues are used for BFS

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)

# Searching a binary search tree

def bst_search(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val: return bst_search(node.left, target)
    else: return bst_search(node.right, target)






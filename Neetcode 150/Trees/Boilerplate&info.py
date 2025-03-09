'''

Both are O(n) space and time


BFS

Commonly used when finding the shortest path 
exploring all nodes at a given level
Commonly implemented with Queue datastructure FIFO manner


DFS

Commonly used when checking if a path exists
Exploring all possible paths
Commonly implemented with a stack with a FILO approach

Preorder traversal - current node, left child, right child
- Used when making a copy of a tree
- Getting a prefix expression

Inorder traversal - left child, current node, right child
- Getting the nodes in a sorted order in a binary search tree (where the left is smaller and right is larger)
- For getting infix expression 

Postorder traversal - left child, right child, current node
- Used when deleting a tree
- Calculating postfix expression
- Calculating size of directories in file

Easy remember:
Pre - before children
In - inbetween children
Post - after children 

Binary search trees are sorted binary trees such that everything on the left of a node is smaller than it and everything right of a node is greater than it
Good at organising things and fast lookup times
BST lookup is O(log2n) - you're just doing binary search basically THIS IS ASSUMING THE TREE IS HEIGHT BALANCED, lopsided trees could be O(n)'''


# Binary trees

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    

# Recursive Pre Order Traversal (DFS)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursive In Order Traversal
def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

# Post order
def post_order(node):
    if not node:
        return
    in_order(node.left)
    in_order(node.right)
    print(node)

# Iterative Pre Order Traversal

def pre_order_iterative(node):
    stk = [node]
    while stk:
        node = stk.pop()
        print(node) # We append the right side first because stacks are FILO and we want to go down the left side first
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)


# Level Order Traversal (BFS)

from collections import deque

def level_order(node):
    q = deque()
    q.append(node) # we have the root on there to begin with

    while q:
        node = q.popleft()
        print(node) # FIFO so we append node left first
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)


# Check if a val exists with DFS

def search(node, target):
    if not node:
        return False
    if node == target:
        return True
    
    return search(node.left, target) or search(node.right, target)


# search BST
def search_bst(node, target):
    if not node:
        return False
    if node == target:
        return True
    
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)

        


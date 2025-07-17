class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def balanced(p, q):
            if not p and not q: # if they're both missing the node then they're essentially the same
                return True
            if (p and not q) or (q and not p): # if one is missing then return false (structural diffs)
                return False
            
            if p.val != q.val: # return false if they aren't the same
                return False
            
            return balanced(p.left, q.left) and balanced(p.right, q.right) # recursive for all child nodes
        return balanced(p,q) # call function
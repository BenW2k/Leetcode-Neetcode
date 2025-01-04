# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Basically you want to use the rabbit and hare technique to determine whether thereis a loop
# This involves using a fast and slow pointer, if there is a loop the fast pointer will eventually be the same as the slow pointer
# if the fast or fast.next pointers (because you'll get an attribute error trying to f.next.next something where the next point is None) are None, then there is no cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = s = head
        
        while f and f.next:
            s = s.next
            f = f.next.next

            if f == s:
                return True
        
        return False
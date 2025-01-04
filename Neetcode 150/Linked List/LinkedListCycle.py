# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = s = head
        
        while f and f.next:
            s = s.next
            f = f.next.next

            if f == s:
                return True
        
        return False
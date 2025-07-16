# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast- slow to find midpoint
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        mid = s.next

        # reverse 2nd half of list
        prev = s.next = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        # Merge lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Basically you want to split the list into two halves, reverse the second half, and then merge the two halves.
# This is due to the the order in which the problem wants to order the list (1,n-1,2,n-2,3,n-3, etc.)
# To find the middle we use the fast and slow pointer technique (fast pointer reaches the end as the slow pointer reaches the middle)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast- slow to find midpoint
        s, f = head, head.next

        while f and f.next: # finding the midpoint
            s = s.next
            f = f.next.next
        
        mid = s.next # mid is s.next (and not s) because fast and sloe usually stops one before the midpoint to enable easy splitting of the linked list

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
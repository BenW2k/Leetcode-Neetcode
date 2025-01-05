# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # create a dummy node because we want to stop the left pointer 1 node before the node we want to remove
        left = dummy # set left pointer to dummy
        right = head #set right to head

        while n > 0: # gives right an offset of n so when right reaches the end the left pointer will be on the node before the nth node
            right = right.next
            n -= 1
        

        while right: #traverse through linked list until right pointer reaches end, moving both left and right
            left = left.next
            right = right.next
        left.next = left.next.next # basically skips the nth node in the linked list after right reaches the end
        
        return dummy.next # we don't want to include the dummy node in our final return statement so we use dummy.next to return the linked list with no dummy node and the nth node removed
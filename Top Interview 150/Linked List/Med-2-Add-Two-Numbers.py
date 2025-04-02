# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Written intuition and solution
# We are seeing that they are stored in reverse order
# Meaning we could reverse the lists, however - this would be computationally expensive and there is likely a better way
# We can just add starting at the ends of the number, use carry over where necessary and insert subsequent numbers at the start of the output list.


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # useful to avoid issues when the first node is going to be changed for any reason
        curr = dummy # set current to dummy
        carry = 0 # initial the carry var

        while l1 or l2 or carry: # This is saying while either list still has elements or carry isnt 0 (for edgecases) execute loop
            # states the val variables with 0 if there is no element in that list anymore
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry # our summation val is the two vals + the potential carry over from the last sum
            carry = val // 10 # smart way of finding the carry over (0 if < 10 else 1)
            val = val % 10 # we only want the second digit for vals over 10 so we use modulo to reflect that
            curr.next = ListNode(val) # instantiates next list node with val

            curr = curr.next # traverses to next node of the output list and input lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # returns dummy.next because we don't want to include the dummy node in our output
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode() # Creates a dummy node for the start of the sorted list to point (it will not really be used beyond this)
        curr = d # initially sets current node to the dummy

        while list1 and list2: # while not at the end of either of list 1 or 2
            if list1.val < list2.val: 
                curr.next = list1 # links current to list 1 by pointing curr.next to the current val of list1
                curr = list1 #sets the current node in the new list to the node of list1
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        curr.next = list1 if list1 else list2 # if list2 reaches the end first it adds all remaining nodes from list1 to the end of the the new list,
                                              # if list1 reaches end first then it adds end of list2, 
                                              # if they're the same length nothing happens because it would only be adding None anyway

        return d.next # returns the linked list beyond d, sort of like a daisy chain, d.next is basically the head of the new list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # create dummy, dummy.next = None
        dummy = ListNoder)

        # starting from node.val = 1
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        
        # dummy -> 1 -> NULL
        # iteration head = 2, dummy.next = 1
        return dummy.next
        
        
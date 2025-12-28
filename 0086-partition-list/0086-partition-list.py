# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessnode = ListNode(0)
        greaternode = ListNode(0)

        lesshead = lessnode
        greaterhead = greaternode

        while head:
            if head.val < x:
                lessnode.next = ListNode(head.val)
                lessnode = lessnode.next
            else:
                greaternode.next = ListNode(head.val)
                greaternode = greaternode.next
            head = head.next
        lessnode.next = greaterhead.next
        greaternode.next = None
        return lesshead.next
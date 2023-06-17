# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        begin=head
        fast=head.next.next
        while fast and fast.next:
            begin=begin.next
            fast=fast.next.next
        begin.next=begin.next.next
        return head

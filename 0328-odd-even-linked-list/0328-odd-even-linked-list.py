# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head
            oddlist=head
            even=oddlist.next
            evenlist=even
            while even and even.next:
                oddlist.next=even.next
                oddlist=oddlist.next

                even.next=oddlist.next
                even=even.next
            oddlist.next=evenlist
            return head
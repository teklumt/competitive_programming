# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        pre=dummy
        while cur:
            if cur.val==val:
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return dummy.next
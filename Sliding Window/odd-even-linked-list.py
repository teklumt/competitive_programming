# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy1=ListNode()
        dummy2=ListNode()
        even=dummy1
        odd=dummy2
        cur=head
        i=1
        while cur:

            if i%2==0:
                even.next=cur
                even=even.next
            else:
                odd.next=cur
                odd=odd.next
            cur=cur.next
            i+=1
        odd.next=dummy1.next
        even.next=None
        return dummy2.next
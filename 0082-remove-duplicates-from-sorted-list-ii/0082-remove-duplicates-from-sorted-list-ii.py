# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        cur=dummy
        while cur:
            if cur.next and cur.next.next and cur.next.val==cur.next.next.val:
                temp=cur.next
                while temp and temp.next and temp.val==temp.next.val:
                    temp=temp.next
                cur.next=temp.next
            else:
                cur=cur.next
        return dummy.next
                
                
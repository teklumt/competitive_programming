# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=head
        k=0
        while cur.next:
            cur=cur.next
            k+=1
        if k%2==0:
            k=k//2
            cur=head
            m=0
            while m<k:
                cur=cur.next
                m+=1
            dummy.next=cur
            return dummy.next
        else:
            k=k//2
            cur=head
            m=0
            while m<=k:
                cur=cur.next
                m+=1
            dummy.next=cur
            return dummy.next


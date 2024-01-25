# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head

        while cur:
            nn=cur
            minn=cur
            while nn:
                if nn.val<minn.val:
                    minn=nn
                nn=nn.next
            temp=cur.val
            cur.val=minn.val
            minn.val=temp
            cur=cur.next
        return head
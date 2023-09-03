# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        num=head
        list1=[]
        while num:
            list1.append(num.val)
            num=num.next
        list1[k-1],list1[-k]=list1[-k],list1[k-1]
        for i in list1:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
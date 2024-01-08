# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        num=head
        list1=[]
        while num:
            list1.append(num.val)
            num=num.next
        if len(list1)==k:
            list1=list1[::-1]
        else:
            for i in range(0,len(list1),+k):
                if len(list1)-i>=k:
                    num=list1[i:i+k]
                    list1[i:i+k]=num[::-1]
        for i in list1:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
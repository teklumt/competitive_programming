# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        num=head
        list1=[]
        while num:
            list1.append(num.val)
            num=num.next
        for i in range(0,len(list1)-1,+2):
            list1[i],list1[i+1]=list1[i+1],list1[i]
        for i in list1:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
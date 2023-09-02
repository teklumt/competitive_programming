# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num2=[]
        num1=[]
        cur1=l1
        cur2=l2
        while cur1:
            num1.append(cur1.val)
            cur1=cur1.next
        while cur2:
            num2.append(cur2.val)
            cur2=cur2.next
        summ1=0
        summ2=0
        for i in num1:
            summ1=summ1*10+i
        for i in num2:
            summ2=summ2*10+i
        summ1=summ1+summ2
        result=[]
        if  summ1!=0:
            while summ1!=0:
                result.append(summ1%10)
                summ1//=10
            result.reverse()

        else:
            result.append(0)
        dummy=ListNode()
        cur=dummy
        for i in result:
            i=ListNode(i)
            cur.next=i
            cur=cur.next
        return dummy.next
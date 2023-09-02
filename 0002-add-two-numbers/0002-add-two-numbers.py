# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                def rev(num):
                        pre=None
                        cur=num
                        while cur:
                            temp=cur.next
                            cur.next=pre
                            pre=cur
                            cur=temp
                        return pre
                num1=rev(l1)
                num2=rev(l2)
                list1=[]
                list2=[]
                while num1:
                    list1.append(num1.val)
                    num1=num1.next
                while  num2:
                    list2.append(num2.val)
                    num2=num2.next
                summ1=0
                summ2=0
                for i in list1:
                    summ1=summ1*10+i
                for i in list2:
                    summ2=summ2*10+i
                summ2+=summ1
                result=[]
                if summ2!=0:
                    while summ2!=0:
                        result.append(summ2%10)
                        summ2//=10
                    result.reverse
                else:
                    result.append(0)
                dummy=ListNode()
                cur=dummy
                for i in result:
                    i=ListNode(i)
                    cur.next=i
                    cur=cur.next
                return dummy.next
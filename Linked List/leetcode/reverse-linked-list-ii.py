# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      
        dummy=ListNode()
        temp=ListNode()
        curd=dummy

        def reverse(head):
            pre=None
            cur=head
            while cur:
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            return pre
        if left==right:
            return head

        cur,First,Last=head,head,head
        
        i=1
        while cur:
            if i!=left:
                temp=cur
            if i==left:
                First=temp
                while i!=right:
                    curd.next=cur
                    curd=curd.next
                    cur=cur.next
                    i+=1
                cur=cur.next
                break
            cur=cur.next
            i+=1
        if curd.next:
            curd.next.next=None
        if First:
            First.next=None
        num=dummy.next
        num=reverse(num)
        rev=num
        while rev and rev.next:
            rev=rev.next
        if left!=1:
            First.next=num
        else:
            head=num
        if rev:
            rev.next=cur

        return head
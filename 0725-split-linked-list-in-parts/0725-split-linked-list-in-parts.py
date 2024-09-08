# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        n=count//k
        left=count%k
        res=[]
        cur=head
        for i in range(k):
            size = n + (1 if left>0 else 0)

            dummy=ListNode(0)
            num=dummy
            for j in range(size):
                if cur:
                    num.next=ListNode(cur.val)
                    cur=cur.next
                    num=num.next
                else:
                    break
            res.append(dummy.next)
            left-=1
        return res

                


            
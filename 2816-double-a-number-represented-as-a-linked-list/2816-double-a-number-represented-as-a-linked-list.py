# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currD = dummy
        res = deque()
        cur = head
        while cur:
            res .append(cur.val)
            cur = cur.next
        # print(res)
        carry  = 0
        for i in  range(len(res)- 1, - 1, -1):
            temp = res[i] * 2 + carry
            if temp > 9:
                res[i] = temp % 10
                carry = 1
            else:
                res[i] = temp 
                carry = 0
        if carry:
            res.appendleft(1)
       
        for i in res:
            currD.next = ListNode(i)
            currD = currD.next
        return dummy.next

        
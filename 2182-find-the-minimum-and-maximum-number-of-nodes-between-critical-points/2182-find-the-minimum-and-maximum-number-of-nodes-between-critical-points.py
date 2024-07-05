# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1,-1]
        arr=[]
        temp=head
        cur=head.next
        i=2
        while cur and cur.next:
            if temp.val < cur.val > cur.next.val:
                arr.append(i)
            elif temp.val > cur.val < cur.next.val:
                arr.append(i)
            i+=1
            temp=cur
            cur=cur.next
        
        if len(arr)<=1:
            return [-1,-1]
        else:
            res=inf
            for i in range(len(arr)-1):
                res=min(res,arr[i+1]-arr[i])

            return [res,arr[-1]-arr[0]]
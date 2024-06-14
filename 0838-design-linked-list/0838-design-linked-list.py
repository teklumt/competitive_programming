class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0      

    def get(self, index: int) -> int:
        cur=self.head
        print(index,self.size)
        if index <self.size:
           
            while index>0:
                cur=cur.next
                index-=1
           
            self._p(self.head)
            return cur.data

        return -1
    def _p(self,head):
        cur=head
        while cur:
            print(cur.data)
            cur=cur.next
        

    def addAtHead(self, val: int) -> None:
        curr=Node(val)
        curr.next=self.head
        self.head=curr
        self.size+=1   
        

    def addAtTail(self, val: int) -> None:
        cur=self.head
        if cur:
            while cur.next:
                cur=cur.next
            cur.next=Node(val)
            self.size+=1    
        else:
            curr=Node(val)
            curr.next=self.head
            self.head=curr
            self.size+=1   

        

    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.head
        newdata=Node(val)
        if index<=self.size:
            
            if index==0:
                newdata.next=self.head
                self.head=newdata
            elif index==self.size:
                while cur.next:
                    cur=cur.next
                cur.next=newdata   
            else:
                while index>1:
                    cur=cur.next
                    index-=1
                newdata.next=cur.next
                cur.next=newdata        
            self.size+=1    

    def deleteAtIndex(self, index: int) -> None:
        if index<self.size:
            if index==0:
                self.head=self.head.next
                self.size-=1
            else:
                cur=self.head
                while index>1:
                    cur=cur.next
                    index-=1
                if cur.next:
                    cur.next=cur.next.next
                else:cur.next=None
                self.size-=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
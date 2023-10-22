class MyCircularDeque:

    def __init__(self, k: int):
        self.data=deque()
        self._len=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.data)==self._len:
            return False
        else:
            self.data.appendleft(value)
            return True


    def insertLast(self, value: int) -> bool:
        if len(self.data)==self._len:
            return False
        else:
            self.data.append(value)
            return True

    def deleteFront(self) -> bool:
        if len(self.data)==0:
            return False
        else:
            self.data.popleft()
            return True        
    
        

    def deleteLast(self) -> bool:
        if len(self.data)==0:
            return False
        else:
            self.data.pop()
            return True       

    def getFront(self) -> int:
        if len(self.data)==0:
            return -1
        else:
            return self.data[0]

        

    def getRear(self) -> int:
        if len(self.data)==0:
            return -1
        else:
            return self.data[-1] 

    def isEmpty(self) -> bool:
        return len(self.data)==0

    def isFull(self) -> bool:
        return len(self.data)==self._len

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
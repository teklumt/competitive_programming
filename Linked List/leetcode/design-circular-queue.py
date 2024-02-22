class MyCircularQueue:

    def __init__(self, k: int):
        self.data=deque()
        self._len=k  

    def enQueue(self, value: int) -> bool:
        if len(self.data)<self._len:
            self.data.append(value)
            return True

    def deQueue(self) -> bool:
        if len(self.data)!=0:
            self.data.popleft()
            # self.data.remove(self.data[0])
            return True

    def Front(self) -> int:
        if len(self.data)==0:
            return -1
        else:
            return self.data[0]        


    def Rear(self) -> int:
        if len(self.data)==0:
            return -1
        else:
            return self.data[-1]              


    def isEmpty(self) -> bool:
        return len(self.data)==0

    def isFull(self) -> bool:
        return len(self.data)==self._len    


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
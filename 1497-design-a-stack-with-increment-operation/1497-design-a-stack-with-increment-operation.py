class CustomStack:

    def __init__(self, maxSize: int):
        self.ind = 0
        self.stack = [-1] * maxSize
    def push(self, x: int) -> None:
        if self.ind < len(self.stack):
            self.stack[self.ind] = x
            self.ind += 1

    def pop(self) -> int:
        if self.ind > 0:
            temp = self.stack[self.ind - 1]
            self.ind -= 1
            return temp
        return -1
                
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k , self.ind)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
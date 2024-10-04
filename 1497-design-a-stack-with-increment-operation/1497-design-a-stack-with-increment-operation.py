class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.increment_ = [0] * maxSize
    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            

    def pop(self) -> int:
        if not self.stack:
            return -1

        lastInc = self.increment_[len(self.stack) - 1]
        res = self.stack.pop() +  lastInc
        if (len(self.stack) - 1) >= 0:
            self.increment_[len(self.stack) - 1] += lastInc
        self.increment_[len(self.stack)] = 0
        return res
        
    def increment(self, k: int, val: int) -> None:
        if (len(self.stack) - 1) >= 0:
            self.increment_[min(k - 1, len(self.stack) - 1)] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
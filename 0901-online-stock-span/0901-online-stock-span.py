class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        b=1
        while self.stack and price>=self.stack[-1][1]:
            count,val=self.stack.pop()
            b+=count
        self.stack.append((b,price))
        return b
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
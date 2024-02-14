class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.cur=0

    def visit(self, url: str) -> None:
        # if self.stack:
        self.stack=self.stack[:self.cur+1]
        self.cur+=1
        self.stack.append(url)
        
        

    def back(self, steps: int) -> str:
        # print()
        # print(self.cur)
        # print(steps)
        if steps <= self.cur:
            self.cur-=steps
        else:
            self.cur=0
        # print(self.cur)
        # print(self.stack)
        return self.stack[self.cur]

    def forward(self, steps: int) -> str:
        if self.cur + steps < len(self.stack):
            self.cur +=steps
        else:
            self.cur = len(self.stack)-1
        return self.stack[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
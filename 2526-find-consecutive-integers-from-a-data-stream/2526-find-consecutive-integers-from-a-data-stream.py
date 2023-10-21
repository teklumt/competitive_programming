class DataStream:

    def __init__(self, value: int, k: int):
        self.hash=dict()
        self.stack=[]
        self.val=value
        self.k=k
        

    def consec(self, num: int) -> bool:
        self.stack.append(num)
        self.hash[num]=self.hash.get(num,0)+1
        if len(self.stack)<self.k:
            return False
        elif len(self.stack)==self.k:
            if self.hash.get(self.val,0)==self.k:
                self.hash[self.stack[0]]-=1
                del self.stack[0]
                return True   
            else:
                self.hash[self.stack[0]]-=1
                del self.stack[0]
                return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
class OrderedStream:

    def __init__(self, n: int):

        self.data=[[]]*n
        self.size=n
        self.ptr=0
        # self.isEmpty=False
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1]=[value]
        res=[]
       
        while self.ptr<self.size and self.data[self.ptr]!=[]:
                res+=self.data[self.ptr]
                self.ptr+=1
            

        return res
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
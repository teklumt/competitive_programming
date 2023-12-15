class FrequencyTracker:

    def __init__(self):
        
        self.store={}
        self.fre={}    

    def add(self, number: int) -> None:
        if number in self.store  and self.store[number] in self.fre:
            self.fre[self.store[number]]-=1
        
        self.store[number]=self.store.get(number,0)+1
        self.fre[self.store[number]]=self.fre.get(self.store[number],0)+1
       

    def deleteOne(self, number: int) -> None:
        if number in self.store:
            if self.store[number] in self.fre and self.fre[self.store[number]]>0:
                self.fre[self.store[number]]-=1
            if self.store[number]!=0:
                self.store[number]-=1
                self.fre[self.store[number]]=self.fre.get(self.store[number],0)+1
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.fre:
            return self.fre[frequency]
        return 0      


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
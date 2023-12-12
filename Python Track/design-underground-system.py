class UndergroundSystem:

    def __init__(self):
        self.checkIns={}
        self.checkOuts={}
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id]=[stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        data = t - self.checkIns[id][1]
        self.checkOuts[self.checkIns[id][0]+'_'+stationName]=self.checkOuts.get(self.checkIns[id][0]+'_'+stationName,[])+[data]
                

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = startStation +'_'+ endStation
        return sum(self.checkOuts[data])/len(self.checkOuts[data])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
class Robot:

    def __init__(self, width: int, height: int):
        
        self.row = height
        self.col = width
        self.cur = [0, 0]
        self.bol=True

    def step(self, num: int) -> None:
        
        self.bol=False
        num=num%(2*(self.row+self.col)-4)
        while num>0:
            if self.cur[1]==0:
                while self.cur[0]<self.col-1 and num>0:
                    self.cur[0]+=1
                    num-=1
            if self.cur[0]==self.col-1:
                while self.cur[1]<self.row-1 and num>0:
                    self.cur[1]+=1
                    num-=1
            if self.cur[1]==self.row-1:
                while self.cur[0]>0 and num>0:
                    self.cur[0]-=1
                    num-=1
            if self.cur[0]==0:
                while self.cur[1]>0 and num>0:
                    self.cur[1]-=1
                    num-=1
        
    def getPos(self) -> List[int]:
        
         return self.cur
        

    def getDir(self) -> str:
        
        if self.bol==True and self.cur==[0,0]:return'East'
        
        # For Four corners
        
        if self.cur==[0,0]:return 'South'
        if self.cur==[self.col-1,0]:return 'East'
        if self.cur==[self.col-1,self.row-1]:return 'North'
        if self.cur==[0,self.row-1]:return 'West'

            
        if self.cur[1]==0:return'East'
        if self.cur[1]==self.row-1:return'West'
        if self.cur[0]==0:return 'South'
        if self.cur[0]==self.col-1:return 'North'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
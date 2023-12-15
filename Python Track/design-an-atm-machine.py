class ATM:

    def __init__(self):
        
        self.store = {20:0,50:0,100:0,200:0,500:0}        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            if i==0:self.store[20]+=20*banknotesCount[i]
            elif i==1: self.store[50]+=50*banknotesCount[i]
            elif i==2: self.store[100]+=100*banknotesCount[i]
            elif i==3: self.store[200]+=200*banknotesCount[i]
            elif i==4: self.store[500]+=500*banknotesCount[i]          
    def withdraw(self, amount: int) -> List[int]:
        pre=deepcopy(self.store)
        res=[0]*5
        if amount >= 500 and pre[500]>0:
            temp=amount//500
            if temp<=pre[500]//500:
                pre[500]-=temp*500
                amount-=temp*500
                res[4]=temp
                
            else:
                nn=pre[500]//500
                amount-=nn*500
                pre[500]-=nn*500
                res[4]=nn

        if amount>=200 and pre[200]>0:
            temp=amount//200
            if temp<=pre[200]//200:
                pre[200]-=temp*200
                amount-=temp*200
                res[3]=temp
            else:
                nn=pre[200]//200
                amount-=nn*200
                pre[200]-=nn*200
                res[3]=nn

        if amount>=100 and pre[100]>0:
            temp=amount//100
            if temp<=pre[100]//100:
                pre[100]-=temp*100
                amount-=temp*100
                res[2]=temp
            else:
                nn=pre[100]//100
                amount-=nn*100
                pre[100]-=nn*100
                res[2]=nn

        if amount>=50 and pre[50]>0:
            temp=amount//50
            if temp<=pre[50]//50:
                pre[50]-=temp*50
                amount-=temp*50
                res[1]=temp
            else:
                nn=pre[50]//50
                amount-=nn*50
                pre[50]-=nn*50
                res[1]=nn

        if amount>=20 and pre[20]>0:
            temp=amount//20
            if temp<=pre[20]//20:
                pre[20]-=temp*20
                amount-=temp*20
                res[0]=temp
            else:
                nn=pre[20]//20
                amount-=nn*20
                pre[20]-=nn*20
                res[0]=nn
       
        if amount!=0:
            return [-1]
        
        self.store=deepcopy(pre)
        
        return res
        
         
        
        
        
        


        

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
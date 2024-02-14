class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count=Counter(customers)
        countY=count['Y']
        countN=0
        res=inf
        final=1
       
        for i in range(len(customers)):
            penality = countY + countN
            if  penality < res:
                res=penality
                final = i
            if customers[i] == 'Y':
                countY-=1
            else:
                countN+=1
        
        return final if res<=min(count['N'],count['Y']) else len(customers)
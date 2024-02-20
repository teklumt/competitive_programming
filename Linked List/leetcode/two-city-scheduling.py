class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # Method I
        costs.sort(key= lambda x:-abs(x[0]-x[1]))
        countA=countB=len(costs)/2
        total=0
        for a,b in costs:
            if countB==0 or (countA and a<=b):
                total+=a
                countA-=1
            else:
                total+=b
                countB-=1
        return total


        # Method II

        a=[]
        b=[]
        res=0
        summa,summb=0,0
        for cost in costs:
            if cost[0]<cost[1]:
                a.append(cost)
                res+=cost[0]
            elif cost[0]>cost[1]:
                b.append(cost)
                res+=cost[1]
            else:
                if len(a)>len(b):
                    b.append(cost)
                else:
                    a.append(cost)
                res+=cost[0]

        if len(a)==len(b):
            return res
        else:
            if a:
                a.sort(key= lambda x:abs(x[0]-x[1]))
            
            if b:
                b.sort(key= lambda x:abs(x[0]-x[1]))

            i=0
            if len(a)>len(b):
                k=abs((len(costs)//2)-len(b))
               
                while k>0:
                    res-=a[i][0]
                    res+=a[i][1]
                    k-=1
                    i+=1
            else:
                k=abs((len(costs)//2)-len(a))
                while k>0:
                    res-=b[i][1]
                    res+=b[i][0]
                    k-=1
                    i+=1
            return res
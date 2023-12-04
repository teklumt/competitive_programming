class Solution:
    def printVertically(self, s: str) -> List[str]:
        mylist=s.split(" ")
        res=[]
        n=0
        for i in mylist:
            n=max(n,len(i))
        for i in range(n):
            num=""
            for j in mylist:
                if i <len(j):
                    num+=j[i]
                else:
                    num+=" "
            res.append(num)
        for i in range(len(res)):
            while res[i][-1]==" ":
                num=list(res[i])
                res[i]="".join(num[:-1])
        return res

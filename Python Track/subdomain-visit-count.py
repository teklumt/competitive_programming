class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res={}
        final=[]
        for i in cpdomains:
            mm=i.split(" ")
            final.append([mm[0],mm[1].split(".")])
        for i in final:
            for j in range(len(i[1])):
                res[".".join(i[1][j:])]=res.get(".".join(i[1][j:]),0)+int(i[0])

        done=[]
        for i in res:
            mm=f"{res[i]} {i}"
            done.append(mm)

        return done
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d=deque()
        r=deque()
        size=len(senate)
        for i in range(len(senate)):
            if senate[i]=='D':
                d.append(i)
            else:
                r.append(i)
        while len(r)!=0 and len(d)!=0:
            if d[0]<r[0]:
                r.popleft()
                d.append(d.popleft()+size)
            else:
                d.popleft()
                
                r.append(r.popleft()+size)
        if len(r)!=0:
            return "Radiant"
        else:
            return "Dire"



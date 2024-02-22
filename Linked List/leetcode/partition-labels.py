class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store=defaultdict()
        for i in range(len(s)):
            store[s[i]]=store.get(s[i],[])+[i]
        store2=[]
        for i in store.values():
            if len(i)==1:
                i.append(i[-1])
                store2.append(i)
            else:
                store2.append(i)
        res=[]
        minn=store2[0][0]
        maxx=store2[0][-1]
        for i in range(1,len(store2)):
            if store2[i][0]<=maxx:
                maxx=max(maxx,store2[i][-1])
            elif store2[i][0]>minn:
                res.append(maxx-minn+1)
                maxx=store2[i][-1]
                minn=store2[i][0]
        res.append(maxx-minn+1)
        return res
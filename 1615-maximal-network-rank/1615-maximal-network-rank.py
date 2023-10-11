class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mydict = collections.defaultdict(list)
        for a, b in roads:
            mydict[a].append(b)
            mydict[b].append(a)
        final = 0
        for i in range(n):
            for j in range(i+1,n):
                length = len(mydict[i])+len(mydict[j])
                if i in mydict[j]:
                    length-=1
                final=max(final,length)
        return final

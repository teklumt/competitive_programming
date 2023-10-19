class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefixsum=[0]
        store={}
        for trip in trips:
            store[trip[1]]=store.get(trip[1],0)+trip[0]
            store[trip[2]]=store.get(trip[2],0)-trip[0]
        result=[]
        for i in store:
            result.append([i,store[i]])
        result.sort()
        for i in result:
            prefixsum.append(prefixsum[-1]+i[1])
        return max(prefixsum)<=capacity
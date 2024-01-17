class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[]
        prisum=[0]
        for trip in trips:
            arr.append([trip[1],trip[0]])
            arr.append([trip[2],-1*trip[0]])
        arr.sort()
        for i in arr:
            prisum.append(prisum[-1]+i[-1])
        print(prisum)

        return max(prisum)<=capacity 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        final=[]
        for n in range(len(points)):
            sum=0
            for m in range(len(points[n])):
                sum=sum+(points[n][m])**2
            result.append([sum,points[n]])
        result.sort()
        for n in range(k):
            final.append(result[n][1])
        return final

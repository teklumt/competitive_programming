class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res=0
        for i in range(0,len(points)-1):
            res1=abs(points[i][0]-points[i+1][0])
            res2=abs(points[i][1]-points[i+1][1])
            res+=max(res1,res2)
        return res
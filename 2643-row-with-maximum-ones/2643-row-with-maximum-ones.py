class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx=0
        res=0
        for i in range(len(mat)):
            m=mat[i].count(1)
            if m>maxx:
                maxx=m
                res=i
        return [res,maxx]
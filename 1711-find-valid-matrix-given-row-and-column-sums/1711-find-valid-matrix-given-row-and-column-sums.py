class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res=[[0]*len(colSum) for i in range(len(rowSum))]
        # return res
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                r=rowSum[i]
                c=colSum[j]

                minn=min(r,c)

                res[i][j]=minn

                rowSum[i]-=minn
                colSum[j]-=minn
        return res

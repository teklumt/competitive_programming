class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j==len(mat)-1:
                    summ+=mat[i][j]
        
        return summ
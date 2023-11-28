class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        res=matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i>=1 and j>=1 and matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
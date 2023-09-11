class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new=[]
        n=len(matrix)
        for i in range(n):
            check=[]
            for j in range(n-1,-1,-1):
                check.append(matrix[j][i])
            matrix.append(check)
        for i in range(n):
            del matrix[0]
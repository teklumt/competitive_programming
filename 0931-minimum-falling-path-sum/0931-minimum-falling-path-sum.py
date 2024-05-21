class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        size=len(matrix)
        for r in range(1,size):
            for c in range(size):

                mid=matrix[r-1][c]
                left=matrix[r-1][c-1] if c>0 else inf
                right=matrix[r-1][c+1] if c<size-1  else inf

                matrix[r][c]+=min(left,mid,right)
        return min(matrix[-1])
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for i in range(row)]
        dp[0] = matrix[0]
        for i in range(col):
            dp[0][i] = int(dp[0][i])
            
        res = 1 if 1 in dp[0] else 0


        for i in range(1, row ):
            for j in range(col):
                if matrix[i][j] == '1':
                    res = max(res, 1)
                if j != 0:
                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i - 1][j] ,dp[i - 1][j - 1] ,dp[i][j - 1]) + 1
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = int(matrix[i][j])
                    
        return res ** 2


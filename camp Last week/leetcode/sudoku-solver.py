class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = []
        
        def backtrack(r, c):
            if r == 9:
                ans.append([row[:] for row in board])
                return
            
            if c == 9:
                backtrack(r + 1, 0)
                return

            if board[r][c] != '.':
                backtrack(r, c + 1)
                return
            
            for i in range(1, 10):
                num = str(i)
                
                seenR = num not in board[r]
                seenC = True
                for j in range(9):
                    if board[j][c] == num:
                        seenC = False
                        break
                
                row = r - r % 3
                col = c - c % 3
                seenRW = True
                for x in range(3):
                    for y in range(3):
                        if board[row + x][col + y] == num:
                            seenRW = False
                            break

                if seenR and seenC and seenRW:
                    board[r][c] = num
                    backtrack(r, c + 1)
                    board[r][c] = '.'

        backtrack(0, 0)
        if ans:
            for i in range(9):
                for j in range(9):
                    board[i][j] = ans[0][i][j]

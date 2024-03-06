class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
       
        def backtrack(r , colSeen, diaSum, dissub):
            if r == n:
                res.append(["".join(rr) for rr in grid])
                return
            

            for j in range(n):
                if (j not in colSeen) and ((r + j) not in diaSum) and ((r - j) not in dissub):
                    grid[r][j] = 'Q'
                   
                    colSeen.add(j)
                    diaSum.add(r + j)
                    dissub.add(r - j)

                    backtrack(r + 1,colSeen, diaSum, dissub)
                    grid[r][j] = '.'

                    
                    colSeen.remove(j)
                    diaSum.remove(r + j)
                    dissub.remove(r - j)

        for i in range(n):
            grid = [['.'] * n  for _ in range(n)]
           
            grid[0][i] = 'Q'

            backtrack(1 , set([i]),set([i]),set([-1*i]))
        return res
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(-1, -1), (1, -1), (-1, 1), (1, 1)]
        
        def isValid(i, j):
            return 0 <= i < row and 0 <= j < col

        def dfs(i, j ,seen):
            if not isValid(i, j) or (i, j) in seen:
                return
            
            seen.add((i, j))
            curr = board[i][j]
            if curr == 'M':
                board[i][j] = 'X'
                return True
            if curr == 'E':
                count = 0
                for r, c in directions:
                    nr = i + r 
                    nc = j + c 
                    if isValid(nr, nc) and board[nr][nc] == 'M':
                        count += 1
                if count != 0:
                    board[i][j] = str(count)
                    return 
                else:
                    board[i][j] = 'B'
                    for r, c in directions: 
                        if dfs(i + r , j + c ,seen):
                            return True
            return False
           
        dfs(click[0], click[1], set())
        return board
        
        
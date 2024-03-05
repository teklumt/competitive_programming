class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        def dfs(r, c, path, seen):
            nonlocal res

            if r < 0 or r >= len(board) or c >= len(board[0]) or c < 0 or (r, c) in seen:
                return 
            

            path += board[r][c]
            seen.add((r, c))
            if word.find(path) == 0:
                if word == path:
                    res = True
                    return
                dfs(r + 1 , c, path, seen.copy())
                dfs(r - 1 , c, path, seen.copy())
                dfs(r, c + 1, path, seen.copy())
                dfs(r , c - 1 , path, seen.copy())
                
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if res:
                    return res
                dfs(i, j, "", set())
        return res
            
            

            
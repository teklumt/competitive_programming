class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        res=0
        visited=set()
        for i in range(len(isConnected)):
            if i not in visited:
                res+=1
                dfs(i)
        return res
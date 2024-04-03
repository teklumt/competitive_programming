class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        color = [-1] * len(isConnected)
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
    
        for i in graph:
            if color[i] == -1:
                res += 1
                color[i] = res
                stack = graph[i]

                while stack:
                    cur = stack.pop()
                    for  j in graph[cur]:
                        if color[j] == -1:
                            color[j] = res
                            stack += graph[j]
        return res





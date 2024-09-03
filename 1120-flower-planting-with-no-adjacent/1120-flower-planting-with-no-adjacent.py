class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u  , v in paths:
            graph[u].append(v)
            graph[v].append(u)

        res = [-1 ] * (n + 1)
        for i in range(1, n + 1):
            if res[i] == -1:
                color = {1 , 2 , 3, 4}
                for nn in graph[i]:
                    if res[nn] in color:
                        color.remove(res[nn])
                res[i] = color.pop()

        return res[1:]
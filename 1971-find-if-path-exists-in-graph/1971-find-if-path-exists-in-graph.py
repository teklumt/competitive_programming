class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        Graph = defaultdict(list)
        for i in edges:
            Graph[i[0]].append(i[1])
            Graph[i[1]].append(i[0])
        res = []
        def dfs(m, visited):
            if m == destination:
                return True
            visited.add(m)
            for i in Graph[m]:
                if i not in visited:
                    if dfs(i, visited):
                        return True
            return False
        
        
        return dfs(source, set())
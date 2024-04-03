class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        Graph = defaultdict(list)
        for i in edges:
            Graph[i[0]].append(i[1])
            Graph[i[1]].append(i[0])
        if not Graph: return True

        stack = [source]
        seen = set([source])

        while stack:
            curNode = stack.pop()

            for i in Graph[curNode]:
                if i == destination:
                    return True
                if i not in seen:
                    stack.append(i)
                    seen.add(i)
        return False
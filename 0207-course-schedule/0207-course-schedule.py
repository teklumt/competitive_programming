class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for i, j  in prerequisites:
            graph[j].append(i)
            indeg[i] += 1
        res = []
        queue = deque()
        for i in range(numCourses):
            if i not in indeg:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            res.append(node)

            for i in graph[node]:
                indeg[i] -= 1
                if not indeg[i]:
                    queue.append(i)
        return len(res) == numCourses

                
            



        
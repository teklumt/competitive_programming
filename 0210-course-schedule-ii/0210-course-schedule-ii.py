class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        count = Counter()
        graph  = defaultdict(list)
        for curr, pre  in prerequisites:
            count[curr] += 1
            graph[pre].append(curr)
            
        queue = deque()
        for i in range(numCourses):
            if i not in count:
                queue.append(i)
        res = []
        seen = set()
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                if count[i] > 0:
                    count[i] -= 1
                    if count[i] == 0:
                        queue.append(i)
                        seen.add(i)
        return res if len(res) == numCourses else []

                


        






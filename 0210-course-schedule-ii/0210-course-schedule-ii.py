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
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                count[i] -= 1
                if count[i] <= 0:
                    queue.append(i)
        return res if len(res) == numCourses else []

                


        






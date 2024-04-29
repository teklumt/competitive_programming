class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        count = Counter()
        for i, j in relations:
            graph[i].append(j)
            count[j] += 1
        
        res = [0] * n
        queue = deque()

        for i in range(1, n + 1):
            if i not in count:
                queue.append(i)
                res[i - 1] = time[i - 1]

        
 
        while queue:
            cur = queue.popleft()
           
            for i in graph[cur]:
                res[i - 1] = max(res[i - 1], res[cur - 1] + time[i - 1]) 
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)
            
        return max(res)

